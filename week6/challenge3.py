from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/users")
def users():
	userlist = str(User.query.all())
	return userlist

@app.route("/users_template")
def usertemp():
	userbullets = []
	u = User.query.filter_by(username='admin').first()
	userbullets.append(u)

	u = User.query.filter_by(username='guest').first()
	userbullets.append(u)

	u = User.query.filter_by(username='leland').first()
	userbullets.append(u)

	# return str(userbullets[0]) + "----" + str(userbullets[1])
	return render_template("usertemp.html", userbullets=userbullets)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return self.username + ' - ' + self.email

if __name__ == "__main__":
    app.run(debug=True)