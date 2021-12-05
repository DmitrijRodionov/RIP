import pyodbc

connectionString = ("Driver={SQL Server Native Client 11.0};"
                    "Server=LAPTOP-EUS1P6PQ\SQLEXPRESS;"
                    "Database=Buildings;"
                    "Trusted_Connection=yes;")

request1 = "SELECT * FROM dbo.City"
request2 = "SELECT * FROM dbo.Building"

connection = pyodbc.connect(connectionString, autocommit=True)
dbCursor = connection.cursor()
dbCursor.execute(request1)
dbCursor.execute(request2)
for row in dbCursor:
    print(f"{row.ID_building} {row.Building_name} {row.Descript} {row.Creation_year}")
connection.commit()
dbCursor.close()
connection.close()