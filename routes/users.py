from flask import render_template, jsonify, request, session, redirect
from . import routes
import requests

@routes.route('/users')
def users():
    if ('savedToken' in session.keys()):
        headers = {'x-auth-token': session['savedToken']}
        data = requests.get('http://localhost:5000/api/v1/users/all', headers=headers)
        data = data.json()
        return render_template('users.html', data_one=data)
    print("Session not started")
    return redirect('/')
