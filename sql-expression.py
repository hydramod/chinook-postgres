from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)
from sqlalchemy.sql import select

# execute instruction from localhost "chinook" db
db = create_engine("postgresql:///chinook")

schema_name = db.dialect.default_schema_name
print(schema_name)

meta = MetaData()

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
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
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
    select_query1 = select([artist_table])

    # Query 2 - select only the Name column from Artists table
    select_query2 = select([artist_table.c.Name])

    # Query 3 - select only Queen from Artists table
    select_query3 = select([artist_table]).where(artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from "Artist" table
    select_query4 = select([artist_table]).where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
    select_query5 = select([album_table]).where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where composer is Queen from the "Track" table
    select_query6 = select([track_table]).where(track_table.c.Composer == "Queen")

    results1 = connection.execute(select_query1)
    for result in results1:
        print(result)

    results2 = connection.execute(select_query2)
    for result in results2:
        print(result)

    results3 = connection.execute(select_query3)
    for result in results3:
        print(result)

    results4 = connection.execute(select_query4)
    for result in results4:
        print(result)

    results5 = connection.execute(select_query5)
    for result in results5:
        print(result)

    results6 = connection.execute(select_query6)
    for result in results6:
        print(result)
