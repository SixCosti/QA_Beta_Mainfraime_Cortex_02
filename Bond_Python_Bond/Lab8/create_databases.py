import pyodbc

def dbquery(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()

    try:
        if statement.startswith('SELECT'):
            result = cur.execute(statement).fetchall()
        else:
            cur.execute(statement)
            conn.commit()
            result = True
        conn.close()
        return result
    except Exception as e:
        print(e)
        conn.close()
        return None

dropTableSQL = """
IF OBJECT_ID('Student', 'U') IS NOT NULL
    DROP TABLE Student
"""

createTableSQL = """
CREATE TABLE Student (
    StudentID INT NOT NULL,
    FirstName NVARCHAR(40) NOT NULL,
    Surname NVARCHAR(30) NULL,
    Course NVARCHAR(30) NULL,
    City NVARCHAR(50) NULL
)
"""

retval = dbquery(dropTableSQL)
print('Dropped the Student Table returned:', retval)

retval = dbquery(createTableSQL)
print('Create the Student Table returned:', retval)

insertQueries = [
    "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (1,'Electra','Pikachu','DevOps','Somewhere Over The Rainbow')",
    "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (2,'Mike','Tyson','Software Development','London')",
    "INSERT INTO Student(StudentID,FirstName,Surname,Course,City) VALUES (3,'Hugh','Rasberry-Pi-Johnson','Rock Star Class','Arkham City')"
]

for insertQuery in insertQueries:
    retval = dbquery(insertQuery)
    print('Inserted:', insertQuery, 'Returned:', retval)

updateQuery = "UPDATE Student SET City = 'London' WHERE FirstName = 'Electra'"
retval = dbquery(updateQuery)
print('Update query returned:', retval)

selectQuery = "SELECT * FROM Student"
selectedRows = dbquery(selectQuery)

for row in selectedRows:
    print(row)
