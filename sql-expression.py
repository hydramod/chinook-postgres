from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#execute intrustion from localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer), 
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:
    
    # Query1 - select all records from Artists table
    # select_query = artist_table.select()

    # Query 2 - select only the Name column from Artists table
    select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - selct only Queen from Artists table
    # cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

    # Query 4 - select only by "ArtistId" #51 from "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

    # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
    # cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" =%s', [51])

    # Query 6 - select all tracks where composer is Queen from the "Track" table
    # cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["Queen"])

    results = connection.execute(select_query)
    for result in results:
        print(result)