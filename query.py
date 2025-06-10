import sqlite3

conn = sqlite3.connect('sales_data.db')
query = """
SELECT product_name, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales_table
GROUP BY product_name
"""
print(conn.execute(query).fetchall())
conn.close()