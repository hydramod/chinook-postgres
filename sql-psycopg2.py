# Import the `psycopg2` module for PostgreSQL database connectivity
import psycopg2

# Establish a connection to the "chinook" database
connection = psycopg2.connect(database="chinook")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Query1 - select all records from Artists table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the Name column from Artists table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - selct only Queen from Artists table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

# Query 6 - select all tracks where composer is Queen from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Queen"])

# Fetch all rows from the result set
results = cursor.fetchall()

# Alternatively, you can use `fetchone()` to retrieve only the first row from the result set
# results = cursor.fetchone()

# Close the database connection
connection.close()

# Iterate over the results and print each row
for result in results:
    print(result)
