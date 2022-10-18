# -------Crear una base de datos
import sqlite3

# crear la bd
conn = sqlite3.connect('pedidos.db')

# crear la bd en memoria
conn = sqlite3.connect(':memory:')

# crear un cursos
cur = conn.cursor()
# cur.execute("CONSULTA")

# -------Conectase a la base de datos

conn = sqlite3.connect('ORDERS.db')
print("Base de datos abierta satisfactoriamente")

# -------Crear tablas

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            userid INT PRIMARY KEY,
            fname TEXT,
            lname TEXT,
            gender TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
            orderid INT PRIMARY KEY,
            date TEXT,
            userid TEXT,
            total TEXT);
""")
conn.commit()
