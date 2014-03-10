from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'
@app.route('/resume/')
@app.route('/resume/<name>')
def hello(name=None):
	return render_template('resume-landing.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)