from flask import render_template, jsonify, request, session, redirect
from . import routes
import requests

@routes.route('/order/<id>')
def order(id):
    if ('savedToken' in session.keys()):
        headers = {'x-auth-token': session['savedToken']}
        data = requests.get('http://localhost:5000/api/v1/orders/{}'.format(id), headers=headers)
        data = data.json()
        return render_template('order.html', data_one=data)
    print("Session not started")
    return redirect('/')

@routes.route('/orders/ordersid/<ids>')
def allOrdersIds(ids):
    if ('savedToken' in session.keys()):
        headers = {'x-auth-token': session['savedToken']}
        data = requests.get('http://localhost:5000/api/v1/orders/ordersid/{}'.format(ids), headers=headers)
        data = data.json()
        return render_template('order.html', data_one=data)
    print("Session not started")
    return redirect('/')

@routes.route('/orders/userid/<uId>')
def ordersByUserId(uId):
    if ('savedToken' in session.keys()):
        headers = {'x-auth-token': session['savedToken']}
        data = requests.get('http://localhost:5000/api/v1/orders/userid/{}'.format(uId), headers=headers)
        data = data.json()
        return render_template('order.html', data_one=data)
    print("Session not started")
    return redirect('/')
