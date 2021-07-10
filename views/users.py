from flask import jsonify, request
from app import mysql
from views import app_views
import jwt


def valid_token(encoded_jwt):
    
    payload = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    user_email = payload.get('email')
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users WHERE email = %s;', [user_email])
    data = cur.fetchall()
    if (data):
        return True
    
    return False
    
def dictUsers(info):
    userInfoDict = {
        "name": info[1],
        "lastname": info[2],
        "govid": info[3],
        "email": info[4],
        "company": info[5]
    }
    return userInfoDict


@app_views.route('/users/all')
def get_all_users():

    token = request.headers.get('x-auth-token')
    isValid = valid_token(token)

    if (isValid):
        cur = mysql.connection.cursor()
        query = 'SELECT * FROM users'
        cur.execute(query)
        
        data = cur.fetchall()
        allUsers = []
        for arrUserData in data:
            theUser = dictUsers(arrUserData)
            allUsers.append(theUser)           
        return jsonify(allUsers)
    return jsonify("INVALID TOKEN")
