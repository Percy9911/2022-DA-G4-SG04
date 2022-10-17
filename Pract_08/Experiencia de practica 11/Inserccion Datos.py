import sqlite3
conn = sqlite3.connect('ORDERS.db')
cur = conn.cursor ()
moreOrders = [(6, '03/10/2021', 3, 2015478), (7, '02/01/2019', 3, 2015698)]
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", moreOrders)
conn.commit()

