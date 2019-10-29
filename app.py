from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Or set inline



@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars_data =mars_data )
	
	#destination_data = mongo.db.collection.find_one()
	#return render_template("index.html", vacation=destination_data)


@app.route("/scrape")
def scrape():
    #mars_data  = mongo.db.mars_data 
    mars= scrape_mars.scrape()
    mongo.db.collection.update({}, mars, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
