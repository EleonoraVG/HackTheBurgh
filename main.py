from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask import url_for

# Flask configurations
app = Flask(__name__, template_folder='templates')
app.config["MONGO_URI"] = "mongodb://hacktheburgh-g46bf.gcp.mongodb.net/test"
mongo = PyMongo(app)

# Load landing page
@app.route('/')
def homepage():
    return render_template("index.html")

#TODO(andrea): change so that user_id does not appear in URL, ie use RESTful api
@app.route("/u/<user_id>")
def userpage(user_id):
    user = mongo.db.users.find_one_or_404({"_id": user_id})
    return render_template("user.html", user=user)

if __name__ == "main":
    app.run()
    app.debug = True
