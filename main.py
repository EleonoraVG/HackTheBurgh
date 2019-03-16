from bson.objectid import ObjectId
from flask import Flask
from flask import render_template
from flask import request
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

# TODO(andrea): Debug only. Remove in prod
@app.route("/u/<user_id>")
def userpage(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("user.html", user=user)

@app.route('/', methods=['POST'])
def user_request():
    data = request.form
    if data and data.get('uid'):
        uid = data.get('uid')
        print(uid)
        user = db.users.find_one({"_id": ObjectId(uid)})
        if user:
            return render_template("user.html", user=user)
    return render_template("index.html", error=True)

if __name__ == "main":
    app.run()
    app.debug = True
