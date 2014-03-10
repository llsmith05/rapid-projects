from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


@app.route("/search", methods=['GET'])
def pets():
	#stub search function to test; only looks at color
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
	#get all arguments
	name = request.args.get('name','')
	breed = request.args.get('breed','')
	color = request.args.get('color','')
	location = request.args.get('location','')

	#build new row and commit session
	newPet = Pet(name, breed, color, location)
	db.session.add(newPet)
	db.session.commit()

	#temp confirm message, no template yet
	return "Added to DB!"

@app.route("/test")
def test():
	#just testing query return data
	record = Pet.query.filter_by(breed="chihuahua").first()
	print record
	return render_template("test.html", record=record)

class Pet(db.Model):
	#builds table def off of existing DB
	__table__ = db.Model.metadata.tables['pets']

	#constructor
	def __init__(self, name, breed, color, location):
		self.name = name
		self.breed = breed
		self.color = color
		self.location = location

	#basic string repr
	def __repr__(self):
		return "Name : " + self.name + " | Breed: " + self.breed + " | Color: " + self.color + " | Location: " + self.location
	

if __name__ == "__main__":
    app.run(debug=True)