from pets2 import db
from pets2 import Pet

db.create_all()

# 
pets = [Pet("Dolce", "chihuahua", "white", "Fort Collins"),
		Pet("Wyatt", "Blue Heeler", "white", "Fort Collins"),
		Pet("Finn", "Golden Retriever", "gold", "Windsor"),
		Pet("Buddy", "Labrador Retriever", "black", "Boulder"),
		Pet("Django", "Bulldog", "tan", "Boulder"),
		Pet("Romeo", "Beagle", "brown", "Denver"),
		Pet("Lily", "Poodle", "white", "Denver"),
		Pet("Bullwinkle", "Boxer", "brown", "Fort Collins"),
		Pet("Violet", "Pug", "black", "Boulder"),
		Pet("Tiberius", "Pit Bull", "white", "Denver")]

db.session.add_all(pets)
db.session.commit()