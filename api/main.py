from flask import Flask, render_template, jsonify, request
import sqlite3
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors=CORS(app)

def get_db_connection():
    conn = sqlite3.connect('system.db')
    return conn

@app.route('/api/customers')
@cross_origin()
def getAllCustomers():
    conexion=get_db_connection()
    cursor=conexion.cursor()
    cursor.execute('SELECT id, firstname, lastname, email, phone, address FROM customers')
    data = cursor.fetchall()
    result = []
    for row in data:
        content = {
                'id':row[0],
                'firstname': row[1],
                'lastname': row[2],
                "email": row[3],
                "phone": row[4],
                "address": row[5]
            }
        result.append(content)
    return jsonify(result)

@app.route('/api/customers/<int:id>')
@cross_origin()
def getCustomer(id):
    conexion=get_db_connection()
    cursor=conexion.cursor()
    cursor.execute('SELECT id, firstname, lastname, email, phone, address FROM customers WHERE id= ' + str(id))
    data = cursor.fetchall()
    content = {}
    for row in data:
        content = {
                'id':row[0],
                'firstname': row[1],
                'lastname': row[2],
                'email': row[3],
                'phone': row[4],
                'address': row[5]
            }
    return jsonify(content)
   
@app.route("/api/customers", methods=["POST"])
def saveCustomer():
    conexion=get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO `customers` (`id`, `firstname`, `lastname`, `email`, `phone`, `address`) VALUES (NULL, ?, ?, ?, ?, ?);",
            (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['address']))
    conexion.commit()
    return "Cliente guardado"


@app.route("/api/customers", methods=["PUT"])
@cross_origin()
def updateCustomer():
    conexion=get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("UPDATE `customers` SET `firstname` = ?, `lastname` = ?, `email` = ?, `phone` = ?, `address` = ? WHERE `customers`.`id` = ?;",
                (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['address'], request.json['id']))
    conexion.commit()
    return "Cliente actualizado"

@app.route('/api/customers/<int:id>', methods=['DELETE'])
@cross_origin()
def removeCustomer(id):
    conexion=get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM `customers` WHERE `customers`.`id` = " + str(id))
    conexion.commit()
    return "Cliente eliminado"

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(None, 3000, True)