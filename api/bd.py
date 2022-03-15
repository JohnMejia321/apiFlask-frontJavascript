import sqlite3

connection = sqlite3.connect('system.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO customers (firstname, lastname, email, phone, address) VALUES (?, ?,?,?,?)",
            ('John', 'mejia',"john@udea.edu.co","1234","cra")
            )

cur.execute("INSERT INTO customers (firstname, lastname, email, phone, address) VALUES (?, ?,?,?,?)",
            ('pedro', 'gomez',"pedro@udea.edu.co","12346777","cra34")
            )



connection.commit()
connection.close()
