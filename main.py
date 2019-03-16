from bson.objectid import ObjectId
from flask import flash
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from pymongo import MongoClient
from wtforms import Form, TextField, TextAreaField, validators, StringField, DateField, SubmitField
from forms import MedicalForm

# Flask configurations
app = Flask(__name__, template_folder='templates')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Mongo config
client = MongoClient("mongodb+srv://hacktheburgh-g46bf.gcp.mongodb.net",
                     username="Admin",
                     password="C8ZRFk4DxIC0iCAe")
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
    return render_template("index.html", message="Error: User not found")

# Load form to fill
@app.route('/new', methods=['GET', 'POST'])
def new_user_form():
    form = MedicalForm(request.form)
    if request.method == 'POST':
        if not form.validate():
            flash('Error: Complete required fields.')
        else:
            data = request.form.to_dict(flat=False)
            print(data)
            outcome = db.user.insert_one(data)
            if outcome.acknowledged:
                return render_template("index.html", message="Success")
    return render_template('form.html', form=form)

if __name__ == "main":
    app.run()
    app.debug = True
