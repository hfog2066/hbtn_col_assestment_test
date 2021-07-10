from flask import render_template, jsonify, request, session, redirect
from . import routes
import requests

@routes.route('/home', methods=['POST', 'GET'])
def home():
    if (request.method == 'POST'):
        optionSelected = request.form['queryOption']

        if optionSelected == 'allUsers':
            return redirect('/users')

        elif optionSelected == 'orderById':
            order_id = request.form['orderId']
            return redirect('/order/{}'.format(order_id))

        elif optionSelected == 'ordersById':
            orders = request.form['ordersByComma']
            return redirect('/orders/ordersid/{}'.format(orders))

        elif optionSelected == 'userOrders':
            user_id = request.form['userId']
            return redirect('/orders/userid/{}'.format(user_id))
            
    return render_template("home.html")