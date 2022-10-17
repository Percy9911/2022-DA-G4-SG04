import sqlite3
conn = sqlite3.connect('orders.db')
print("Base de datos abierta satisfactoriamente");
cur = conn.cursor()
cur.execute("SELECT * FROM orders;")
five_results = cur.fetchmany(5)
print(five_results)
print("Consulta realizada satisfactoriamente");
conn.close()