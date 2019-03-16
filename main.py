from bson.objectid import ObjectId
from flask import Flask, render_template
from flask import url_for
from pymongo import MongoClient

# Flask configurations
app = Flask(__name__, template_folder='templates')

# Mongo config
client = MongoClient("mongodb+srv://hacktheburgh-g46bf.gcp.mongodb.net",
                     username="Patient",
                     password="p7YtekN64Z5yO03g")
db = client.hacktheburgh

# Load landing page
@app.route('/')
def homepage():
    return render_template("index.html")

#TODO(andrea): change so that user_id does not appear in URL, ie use RESTful api
@app.route("/u/<user_id>")
def userpage(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("user.html", user=user)

if __name__ == "main":
    app.run()
    app.debug = True
