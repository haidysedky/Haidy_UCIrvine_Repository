from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
	mars_data_py = mongo.db.mars_data.find_one()
	return render_template("index.html", mars_data_dict= mars_data_py)

@app.route("/scrape")
def scraper():
	mars_info = mongo.db.mars_data
	data = scrape_mars.scrape()
	mars_info.update({}, data, upsert=True)
	return redirect("/", code=302)

if (__name__ == "__main__"):
	app.run(debug=True)