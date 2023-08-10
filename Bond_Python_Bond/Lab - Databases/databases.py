import pyodbc  # We need the module to connecto the db

# We set up an object to describe how to connect to the DB
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
# We open the connection to the database (like opening a file)
# This creates an intermediate DB object
conn = pyodbc.connect(connectionString)
# We use our new object to create another object called a cursor
# They cursor can send SQL commands to the DB
cur = conn.cursor()
# We send a command to the DB and save the result
result = cur.execute('SELECT * FROM company').fetchall()
# We close the connection
#conn.close()
# We display the result we saved

company_name = 'TechCompany'
cur.execute("SELECT * FROM company WHERE company_name ")
result = cur.fetchall()
print(result)

cur.close()
conn.close()

for row in result:
    print(row)