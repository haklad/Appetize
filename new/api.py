import requests
from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
import json
from bson import json_util
import base64
import datetime
from flask_cors import CORS
import flask

print(flask.__version__)
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'food'
app.config['MONGO_URI'] = "mongodb://localhost/food"
CORS(app)
mongo = PyMongo(app)

@app.route('/<name>/<message>/<rest>', methods=['POST'])
def insert(name,message,rest):
    com = mongo.db.comments
    print(list(com.find()))
    uid = com.insert({"name":name,"message":message, "restaurant":rest})
    print(uid)
    req = request.json
    print(req,name,message)
    docs_list = list(com.find())
    output=[]
    for i in docs_list:
        output.append({i['_id']: [i['name'],i['message']]})
    return jsonify({"output": output})

@app.route('/<id>', methods=['DELETE'])
def delete(id):
    com = mongo.db.comments
    u = com.remove({"_id":id})
    print(u)
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
