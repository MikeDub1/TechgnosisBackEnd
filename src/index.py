from flask import Flask, request, Response
from flask_cors import CORS

storage = {"DEADLYHIPPO4": "Ssbu2018", "MigzLeon":"Migz", "240FPS-girl": "password"}
count = 0

app = Flask(__name__)
CORS(app)

@app.route("/signIn")
def hello():
    username = request.args.get("Username")
    password = request.args.get("Password")

    if (username, password) in storage.items():
        return Response(status=200)
    else:
        return Response(status=404)



     
