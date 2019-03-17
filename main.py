# [START gae_python37_app]
import requests

from bson.objectid import ObjectId
from flask import flash
from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient
from wtforms import Form, TextField, TextAreaField, validators, StringField, DateField, SubmitField
from forms import MedicalForm

app = Flask(__name__, template_folder='templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Mongo config
client = MongoClient("mongodb://hacktheburgh-shard-00-00-g46bf.gcp.mongodb.net:27017,hacktheburgh-shard-00-01-g46bf.gcp.mongodb.net:27017,hacktheburgh-shard-00-02-g46bf.gcp.mongodb.net:27017/test?ssl=true&replicaSet=HackTheBurgh-shard-0&authSource=admin&retryWrites=true/removeme", username="Admin", password="C8ZRFk4DxIC0iCAe")

db = client.hacktheburgh

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def homepage():
    data = request.form
    print("the data:")
    print(data)
    if data and data.get('uid'):
        uid = data.get('uid')
        print(uid)
        user = db.users.find_one({"_id": ObjectId(uid)})
        if user:
           print("user found")
           return render_template("user.html", user=user)
    if data:
        print("user not found")
        return render_template("index.html", message="Error: User not found")
    return render_template("index.html")

# TODO(andrea): Debug only. Remove in prod
@app.route("/u/<user_id>")
def userpage(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("user.html", user=user)

# Load form to fill
@app.route('/new', methods=['GET', 'POST'])
def new_user_form():
    form = MedicalForm(request.form)
    if request.method == 'POST':
        if not form.validate():
            flash('Error: Complete required fields.')
        else:
            data = request.form.to_dict(flat=True)
            outcome = db.users.insert_one(data)
            if outcome.acknowledged:
                uid = str(outcome.inserted_id)
                print(uid)
                flash('Success: User added to Database. You can now write the NFC Tag.')
                return render_template('form.html', form=form, uid=uid)
    return render_template('form.html', form=form, uid=False)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python37_app]
