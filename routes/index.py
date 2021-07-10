from flask import render_template, jsonify, request, session, redirect
from . import routes
import requests

@routes.route('/', methods=['POST', 'GET'])
def login():

    if (request.method == 'POST'):
        email = request.form['logemail']
        psw = request.form['logPassword']
        
        data = requests.post('http://localhost:5000/api/v1/login/', json={ 'email': email, 'password': psw })
        
        if (data.status_code == 200):
            data = data.json()
            session['savedToken'] = data.get('TOKEN')
            return redirect('/home')
        print("INVALID USER OR EMAIL!!!")
        return redirect('/')
        
    session.clear()
    return render_template('index.html')

@routes.route('/signup')
def signup():
    return render_template('signup.html')

@routes.route('/signupinfo', methods=['POST'])
def signupInfo():
    if request.method == 'POST':

        userInfo = {
        "name": request.form['signName'],
        "lastname": request.form['signLastname'],
        "govid": request.form['signGovid'],
        "email": request.form['signEmail'],
        "company": request.form['signCompany'],
        "password": request.form['signPassword']
        }
        """
        name = request.form['signName']
        lastname = request.form['signLastname']
        govid = request.form['signGovid']
        email = request.form['signEmail']
        company = request.form['signCompany']
        password = request.form['signPassword']
        """
        data = requests.post('http://localhost:5000/api/v1/signup/', json=userInfo)
        if data.status_code == 200:
            data = data.json()
            print("DATA", data)
            return redirect('/')
            
        return redirect(url_for('Index'))
