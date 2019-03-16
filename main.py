from flask import Flask, render_template
from flask import url_for
from pymongo import MongoClient

# Flask configurations
app = Flask(__name__, template_folder='templates')

# Mongo config
client = MongoClient("mongodb+srv://hacktheburgh-g46bf.gcp.mongodb.net")
db = client.hacktheburgh

# Load landing page
@app.route('/')
def homepage():
    return render_template("index.html")

#TODO(andrea): change so that user_id does not appear in URL, ie use RESTful api
@app.route("/u/<user_id>")
def userpage(user_id):
    print(user_id)
    user = db.users.find({"_id": user_id})
    return render_template("user.html", user=user)

if __name__ == "main":
    app.run(host='127.0.0.1', port=8080, debug=True)
    app.debug = True
