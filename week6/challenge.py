from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Placeholder"

@app.route("/home")
def home():
	nav1 = nav()
	nav1.title = "Work"
	nav1.href = "http://www.changemakers.com"

	nav2 = nav()
	nav2.title = "Twitter"
	nav2.href = "http://www.twitter.com"

	nav3 = nav()
	nav3.title = "Facebook"
	nav3.href = "http://www.facebook.com"

	navigation = [nav1, nav2, nav3]
	subtitle = "Welcome to my webpage"
	return render_template('home.html', navigation=navigation, subtitle=subtitle)

class nav:
	title = ""
	href = ""

if __name__ == "__main__":
    app.run(debug=True)