from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask_pet_db import Pet

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_pets2.db'
db = SQLAlchemy(app)

@app.route('/detail/')
@app.route('/detail/<id>')
def detail(id=None):
    if id == None:
        return render_template('detail.html', item=None)
    else:
        return render_template('detail.html', item=Pet.query.filter_by(id=id).first())

@app.route("/addpet")
def addpet():
    return render_template("add.html")

@app.route("/add", methods=['GET'])
def add():
    #get all arguments
    name = request.args.get('name','')
    species = request.args.get('species','')
    color = request.args.get('color','')
    gender = request.args.get('gender','')
    latitude = request.args.get('latitude','')
    longitude = request.args.get('longitude','')
    url = request.args.get('url','')

    #build new row and commit session
    newPet = Pet(name, species, color, gender, latitude, longitude, url)
    db.session.add(newPet)
    db.session.commit()

    #temp confirm message, no template yet
    return "Added to DB!"

@app.route('/search', methods=['GET'])
def find():
    count = request.args.get('n')
    if count:
        count = int(count)

    pets = Pet.query.all()

    name = request.args.get('name')
    if name == None:
        pass

    species = request.args.get('species')
    if species == None:
        pass

    color = request.args.get('color')
    if color == None:
        pass

    gender = request.args.get('gender')
    if gender == None:
        pass

    latitude = request.args.get('latitude')
    if latitude == None:
        pass

    longitude = request.args.get('longitude')
    if longitude == None:
        pass

    url = request.args.get('url')
    if longitude == None:
        pass

    kwargs = {}
    if name: kwargs['name']=name
    if species: kwargs['species']=species
    if color: kwargs['color']=color
    if gender: kwargs['gender']=gender
    if latitude: kwargs['latitude']=latitude
    if longitude: kwargs['longitude']=longitude
    if url: kwargs['url']=url

    pets = Pet.query.filter_by(**kwargs)

    return render_template('search.html', list=pets)


if __name__ == '__main__':
    app.run(debug=True)