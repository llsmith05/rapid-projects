import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Led Zeppelin")
new_artist.albums = [Album("I", "Atlantic", "Rock", "CD")]
 
# add more albums
more_albums = [Album("II", "Atlantic", "Rock", "CD"),
               Album("Houses of the Holy", "Atlantic", "Rock", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("alt-J"),
    Artist("Rolling Stones"),
    Artist("Lucius")
    ])
session.commit()