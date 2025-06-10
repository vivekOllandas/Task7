import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('sales_data.db')

# Define and run the query
query = """
SELECT product_name AS product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales_table
GROUP BY product_name
"""
df = pd.read_sql_query(query, conn)

# Print the DataFrame
print(df)

# Plot the bar chart
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product', legend=False)
plt.ylabel('Revenue')
plt.tight_layout()

# Save the chart
plt.savefig("sales_chart.png")
plt.show()

# Optional: Show the chart
# plt.show()

# Close connection
conn.close()
