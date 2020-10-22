import firebase_admin
from flask import Flask, request, Response
from flask_cors import CORS
from firebase_admin import auth, credentials, storage, firestore
from flask_pymongo import PyMongo




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Techgnosis"
CORS(app)


cred = credentials.Certificate('../firebaseAuthentication.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://techgnosisda.firebaseio.com/'})
auth = firebase_admin.auth
mongodb = PyMongo(app)


@app.route("/api/signIn")
def hello():
    print("hello!")
import techgnosisAPI.FirebaseCrudUsers


     
