from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_pets2.db'
db = SQLAlchemy(app)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    species = db.Column(db.String(80), unique=False)
    color = db.Column(db.String, unique=False)
    gender = db.Column(db.String(80), unique=False)
    latitude = db.Column(db.Float, unique=False)
    longitude = db.Column(db.Float, unique=False)
    url = db.Column(db.String(80), unique=False)

    def __init__(self, name, species, color, gender, latitude, longitude, url):
        self.name = name
        self.species = species
        self.color = color
        self.gender = gender
        self.latitude = latitude
        self.longitude = longitude
        self.url = url

    def __repr__(self):
        return 'Name:%s, Species:%s, Color:%d, Gender:%s, Lat:%f, Long:%f, URL:%s' % (self.name, self.species, self.color, self.gender, self.latitude, self.longitude, self.url)