import firebase_admin
import bcrypt
import os
import requests
import json
from flask import Flask, request, Response, jsonify, abort
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
os.environ["FIREBASE_WEB_API_KEY"] = "AIzaSyBoCdMgCwzTldKyVCq_6Gp42cl16NFDNv8"

signin_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

@app.errorhandler(404)
def resourceNotAvailable(e):
    return jsonify(status_code=404, message=str(e)), 404

@app.route("/api/signIn", methods=['GET'])
def signIn():
    uname = request.args.get("Username")
    password = request.args.get("Password")
    user = mongodb.db.users.find_one({"Username" : uname})

    if not user:
        return abort(404, description="The user does not exist!!!")

    if not bcrypt.checkpw(password.encode('utf-8'), user.get("Password")):
        return abort(404, description="The password is incorrect.")

    payload = json.dumps({
        "email" : user.get("Email"),
        "password" : password,
        "returnSecureToken": True
    })

    r = requests.post(signin_api_url, params={"key": os.environ["FIREBASE_WEB_API_KEY"]}, data=payload)

    dictionary  = r.json()
    dictionary["status_code"] = 200
    return json.dumps(dictionary)

import techgnosisAPI.FirebaseCrudUsers


     
