from firebase_admin import exceptions
from firebase_admin.exceptions import FirebaseError
from flask import Flask, request, Response
from techgnosisAPI import app, mongodb, auth
import bcrypt

#EMAIL VERIFICATION!!!
@app.route("/api/signUp", methods=['POST'])
def createUser():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    email = request.args.get("email")
    uname = request.args.get("uname")
    date_of_birth = request.args.get("dateOfBirth")
    country_of_residence = request.args.get("countryOfResidence")
    password = request.args.get("password")

    try:
        user = auth.create_user(email=email, password=password)
        print(user)

        users = mongodb.db.users
        hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert({'First Name':fname, 'Last Name':lname,'Email':email, 'Username':uname, 'DOB':date_of_birth, 'Country of Residence':country_of_residence, 'Password': hashpass})



    except FirebaseError:
        return FirebaseError.cause

    return Response(status=200)

