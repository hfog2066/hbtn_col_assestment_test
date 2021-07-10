from flask import jsonify, request
from app import mysql
from api.v1.views import app_views
import jwt


def valid_token(encoded_jwt):
    try:
        payload = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
        user_email = payload.get('email')
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE email = %s;', [user_email])
        data = cur.fetchall()
        if (data):
            return True
    except:
        return False

def dictOrders(info):
    orderInfoDict = {
        "orderdate": info[1],
        "ordertotal": info[2],
        "ordersubtotal": info[3],
        "ordertaxes": info[4],
        "orderpaid": info[5]
    }
    return orderInfoDict

@app_views.route('/orders/<id>')
def get_order_by_id(id):

    token = request.headers.get('x-auth-token')
    isValid = valid_token(token)

    if(isValid):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM orders WHERE orderid = %s;', [id])
        
        data = cur.fetchall()
        myOrder = []
        for arrOrderData in data:
            theOrder = dictOrders(arrOrderData)
            myOrder.append(theOrder)
        return jsonify(myOrder)
        """
        return jsonify({
            "orderid": data[0][0],
            "date": data[0][1],
            "total": data[0][2],
            "subtotal": data[0][3],
            "taxes": data[0][4],
            "paid": data[0][5]
        })
        """
    return jsonify("INVALID TOKEN")


@app_views.route('/orders/ordersid/<orders_id>')
def get_orders_by_orderid(orders_id):

    token = request.headers.get('x-auth-token')
    isValid = valid_token(token)

    if(isValid):
        cur = mysql.connection.cursor()
        strIds = orders_id
        arrIds = []
        twoDigitid = ""
        count = 0

        allOrders = []

        for c in strIds:
            if c is ",":
                count = count + 1
                cur.execute('SELECT * FROM orders WHERE orderid = %s;', [twoDigitid])
                
                data = cur.fetchall()
                
                for arrOrderData in data:
                    theOrder = dictOrders(arrOrderData)
                    allOrders.append(theOrder)

                arrIds.append(data[0])
                twoDigitid = ""
                continue
            count = count + 1
            twoDigitid = twoDigitid + c
            if(count == len(strIds)):
                cur.execute('SELECT * FROM orders WHERE orderid = %s;', [twoDigitid])
                
                data = cur.fetchall()

                for arrOrderData in data:
                    theOrder = dictOrders(arrOrderData)
                    allOrders.append(theOrder)

                arrIds.append(data[0])
        
        return jsonify(allOrders)
    return jsonify("INVALID TOKEN")


@app_views.route('/orders/userid/<user_id>')
def get_order_by_userid(user_id):

    token = request.headers.get('x-auth-token')
    isValid = valid_token(token)

    if(isValid):
        allOrders = []
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM orders WHERE userid = %s;', [user_id])
        
        data = cur.fetchall()
        for ordersInfo in data:
            theOrder = dictOrders(ordersInfo)
            allOrders.append(theOrder)
        return jsonify(allOrders)
    return jsonify("INVALID TOKEN")
