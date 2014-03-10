from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/find', methods=['PUT', 'GET', 'POST'])
def find():
	if request.method == 'GET':
		course = request.args.get('course')
		if course == 'CSCI1300':
				return "Find the classroom for CSCI1300 ... ATLAS 100"
		elif course == 'CSCI2240':
				return "Find the classroom for CSCI2240 ... ITTL 1B50"
		else:
				return "Sorry no result for " + course
	else:
		return 'Sorry, bad request'

@app.route('/notification')
def notification():
	return 'Get notification. To be implemented'

if __name__ == '__main__':
    app.run(debug=True)