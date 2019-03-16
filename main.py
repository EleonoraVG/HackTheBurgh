# [START gae_python37_app]
from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import request

app = Flask(__name__, template_folder='templates')

# Mongo config
client = MongoClient("mongodb://hacktheburgh-shard-00-00-g46bf.gcp.mongodb.net:27017,hacktheburgh-shard-00-01-g46bf.gcp.mongodb.net:27017,hacktheburgh-shard-00-02-g46bf.gcp.mongodb.net:27017/test?ssl=true&replicaSet=HackTheBurgh-shard-0&authSource=admin&retryWrites=true/removeme", username="Admin", password="C8ZRFk4DxIC0iCAe")
db = client.hacktheburgh

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/u/<user_id>")
def userpage(user_id):
        user = db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("user.html", user=user)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
