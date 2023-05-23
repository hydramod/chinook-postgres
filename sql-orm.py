from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# execute instruction from localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create class based model for "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create class based model for "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create class based model for "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# create new session instance
Session = sessionmaker(db)
# Opens session
session = Session()

# creat database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all record from "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the Name column from Artists table
artists = session.query(Artist.Name)
for artist in artists:
    print(artist.Name)

# Query 3 - select only Queen from Artists table
artists = session.query(Artist).filter(Artist.Name == "Queen")
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from "Artist" table
artist = session.query(Artist).get(51)
if artist:
    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
albums = session.query(Album).filter(Album.ArtistId == 51)
for album in albums:
    print(album.AlbumId, album.Title, sep=" | ")

# Query 6 - select all tracks where composer is Queen from the "Track" table
tracks = session.query(Track).filter(Track.Composer == "Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )


