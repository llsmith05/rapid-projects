from sqlalchemy import Column, Date, Integer, String
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet.db'
db = SQLAlchemy(app)

#Pet table definitions
class Pet(db.Model):
	# """"""
	# __tablename__ = "pets"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	breed = db.Column(db.String)
	color = db.Column(db.String)
	location = db.Column(db.String)

	def __init__(self, name, breed, color, location):
		# """"""
		self.name = name
		self.breed = breed
		self.color = color
		self.location = location

	# def __repr__():
	# 	return self.name + " | " + self.breed + " | " + self.color + " | " + self.location


@app.route("/search", methods=['GET'])
def pets():
	results = []
	arg1 = request.args.get('breed', '')
	results = Pet.query.filter_by(breed=arg1)
	return results

@app.route("/test")
def test():
	row1 = Pet.query.filter_by(breed="chihuahua")
	return row1[0]

if __name__ == "__main__":
    app.run(debug=True)