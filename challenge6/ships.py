from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ships.db'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


@app.route("/search", methods=['GET'])
def pets():
	arg1 = request.args.get('color', '')
	results = Pet.query.filter_by(color=arg1).all()	
	c = Pet.query.filter_by(color=arg1).count()
	
	# test stuff
	# for i in range(0, c):
	# 	print results[i]

	return render_template("search.html", record=results)

@app.route("/addpet")
def addpet():
	return render_template("add.html")

@app.route("/add", methods=['GET'])
def add():
	name = request.args.get('name','')
	breed = request.args.get('breed','')
	color = request.args.get('color','')
	location = request.args.get('location','')

	newPet = Pet(name, breed, color, location)
	db.session.add(newPet)
	db.session.commit()

	return "Added to DB!"

@app.route("/test")
def test():
	record = Pet.query.filter_by(breed="chihuahua").first()
	print record
	return render_template("test.html", record=record)

class Ship(db.Model):
	__table__ = db.Model.metadata.tables['ships']

	def __init__(self, name, model):
		self.name = name
		self.model = model

	def __repr__(self):
		return "Name : " + self.name + " | Model: " self.model

class Crew(db.Model):
	__table__ = db.Model.metadata.tables['members']

	def __init__(self, name, title, race, ship):
		self.name = name
		self.title = title
		self.race = race
		self.ship = ship

	def __repr__(self):
		return "Name : " + self.name + " | Title: " self.title
	

if __name__ == "__main__":
    app.run(debug=True)