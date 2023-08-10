import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()


insertquery = "INSERT INTO company (company_no,company_name,tel,county,post_code) VALUES (4500,'QA','01234 567890','London','W1 1AA')"
conn.commit()

update_query = "UPDATE company SET county = 'West London' WHERE county = 'London'"
cur.execute(update_query)
conn.commit()
mic_check1 = "SELECT * FROM company WHERE county = 'West London'"
fetch1 = cur.execute(mic_check1).fetchall()
mic_check2 = "SELECT * FROM company WHERE county = 'London'"
fetch2 = cur.execute(mic_check2).fetchall()



delete_query = "DELETE FROM salesperson WHERE first_name = 'Inge'"
cur.execute(delete_query)
conn.commit()

mic_check3 = "SELECT * FROM salesperson WHERE first_name = 'Inge'"
fetch3 = cur.execute(mic_check3).fetchall()


cur.close()
conn.close()

print(fetch1, "\n--------------------------------------")
print(fetch2, "\n--------------------------------------")
print(fetch3, "\n--------------------------------------")
print("Task failed successfully!")