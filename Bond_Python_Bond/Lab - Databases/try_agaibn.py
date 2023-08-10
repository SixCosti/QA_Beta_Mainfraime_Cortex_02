import pyodbc

# Connection string
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

# Open the connection to the db
conn = pyodbc.connect(connectionString)

# Create the cursor 
cur = conn.cursor()

# Filtering SELECT statements
result = cur.execute("SELECT company_no, company_name FROM company WHERE county='London'").fetchall()
result1 = cur.execute("SELECT dept_no, dept_name FROM dept WHERE dept_no < 2005").fetchall()
result2 = cur.execute("SELECT order_value, contact_code FROM sale WHERE order_value BETWEEN 5 AND 350").fetchall()
result3 = cur.execute("SELECT first_name, last_name FROM salesperson WHERE first_name LIKE '%tie'").fetchall()
#result4 = cur.execute("SELECT * FROM salesperson").fetchall()

# Close the cursor and the connection (!must remember to close!)
cur.close()
conn.close()

# Displaying my findings
for item in result:
    print(item)
print('---')
for item in result1:
    print(item)
print('---')
for item in result2:
    print(item)
print('---')
for item in result3:
    print(item)
print('---')
#for item in result4:
 #   print(item)
#print('---')
