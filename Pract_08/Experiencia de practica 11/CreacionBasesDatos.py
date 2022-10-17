import sqlite3
conn = sqlite3.connect('ORDERS.db')
cur = conn.cursor ()
print("Base de datos abierta satisfactoriamente");
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS ORDERS(
 orderid INT PRIMARY KEY,
 date TEXT,
 userid TEXT,
 total TEXT);
""")
conn.commit()

