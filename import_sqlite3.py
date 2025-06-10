import sqlite3 
conn = sqlite3.connect('sales_data.db')
print(conn.execute("select * from sales_table").fetchall())
conn.close()