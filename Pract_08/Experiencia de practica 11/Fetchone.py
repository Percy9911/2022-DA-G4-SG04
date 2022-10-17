import sqlite3
conn = sqlite3.connect('orders.db')
print("Base de datos abierta satisfactoriamente");
cur = conn.cursor()
cur.execute("SELECT * FROM orders;")
one_result = cur.fetchone()
second_result = cur.fetchone()
third_result = cur.fetchone()
print(one_result)
print(second_result)
print(third_result)
print("Consulta realizada satisfactoriamente");
conn.close()