# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:40:42 2019

@author: ssak3
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({"You've sent": some_json})
    else:
        return jsonify({"about": "Hello World!"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_muliplied_by_10(num):
    return jsonify({'result': num * 10})


if __name__ == "__main__":
    app.run(debug=True)
