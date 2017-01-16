from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/euler")
@app.route("/euler/<int:problem>")
def euler(problem=None):
	if problem is not None:
		try:
			return render_template("/euler/problem{}.html".format(problem))
		except:
			return render_template("404.html")

	return render_template("euler.html")

@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


if __name__ == '__main__':
	app.run(debug=True)