from flask import json, jsonify, request
from app import mysql
from api.v1.views import app_views
import jwt


@app_views.route('/signup/', methods=['POST'])
def signup():

    args = request.get_json()
    
    name = args.get("name")
    lastname = args.get("lastname")
    govid = args.get("govid")
    email = args.get("email")
    company = args.get("company")
    password = args.get("password")
     
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO users (name, lastname, govid, email, company, password) VALUES (%s, %s, %s, %s, %s, %s)', (name, lastname, govid, email, company, password))

    mysql.connection.commit()
    return jsonify("REGISTERED SUCCESFULLY")

@app_views.route('/login/', methods=['POST'])
def login():

    args = request.get_json()

    useremail = args.get("email")
    password = args.get("password")
    cur = mysql.connection.cursor()

    exist = cur.execute('SELECT * FROM users WHERE email = %s AND password = %s;', (useremail, password))

    if (exist == 1):
        encoded_jwt = jwt.encode({"email": useremail}, "secret", algorithm="HS256")
        return jsonify({"TOKEN": encoded_jwt})  

    
