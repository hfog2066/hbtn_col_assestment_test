#!/usr/bin/python3
from flask import render_template
from views import app_views
from flask import Flask, jsonify
from flask import MySQL

#Initialization
app = Flask(__name__)


app.register_blueprint(app_views)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'companydb'
mysql = MySQL(app)



@app.errorhandler(404)
def invalid_route(e):
    """Handle 404 error with json response 404"""
    return jsonify(error="Not found"), 404

if __name__ == '__main__':
    
    app.run(port=5000, threaded=True, debug=True)

