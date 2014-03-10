from flask import Flask
from flask import render_template
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///crews.db', echo=True)
Base = declarative_base()
Base.metadata.drop_all(engine)

########################################################################
class Ship(Base):
    """"""
    __tablename__ = "ships"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)  
    model = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, name, model):
        """"""
        self.name = name
        self.model = model    
 
########################################################################
class Member(Base):
    """"""
    __tablename__ = "members"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    title = Column(String)
    race = Column(String) 
    ship_name = Column(String, ForeignKey("ships.name"))
    ship = relationship("Ship", backref=backref("members", order_by=id))
 
    #----------------------------------------------------------------------
    def __init__(self, name, title, race):
        """"""
        self.title = title
        self.name = name
        self.race = race
 
# create tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

ship1 = Ship("Discovery", "XD-1")
members1 = [Member("HAL", "AI", "Synthetic"),
			Member("Frank", "Pilot", "Human"),
			Member("Dave", "Pilot", "Human")]		
ship1.members.extend(members1)

ship2 = Ship("Normandy", "SR-2")
members2 = [Member("EDI", "AI", "Synthetic"),
			Member("Shepherd", "Captain", "Human"),
			Member("Tali", "Engineer", "Quarian"),
			Member("Mordin", "Doctor", "Salarian"),
			Member("Garrus", "Operative", "Turian")]			
ship2.members.extend(members2)

session.add(ship1)
session.add(ship2)
session.commit()

app = Flask(__name__)
	
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()
