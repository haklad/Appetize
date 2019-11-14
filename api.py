import requests
from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
import json
from bson import json_util
import base64
import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'food'
app.config['MONGO_URI'] = "mongodb://localhost/food"
CORS(app)
mongo = PyMongo(app)


def time_elapsed_string(datetime, full = False):
	# now = new DateTime;
	# ago = new DateTime('@' . datetime);
	# diff = now->diff(ago);
    #
	# diff->w = floor(diff->d / 7);
	# diff->d -= diff->w * 7;
    #
	# string = array(
	# 	'y' => 'year',
	# 	'm' => 'month',
	# 	'w' => 'week',
	# 	'd' => 'day',
	# 	'h' => 'hour',
	# 	'i' => 'minute',
	# 	's' => 'second',
	# );
	# foreach (string as k => &v) {
	# 	if (diff->k) {
	# 		v = diff->k . ' ' . v . (diff->k > 1 ? 's' : '');
	# 	} else {
	# 		unset(string[k]);
	# 	}
	# }
    #
	# if (!full) string = array_slice(string, 0, 1);
	# return string ? implode(', ', string) . ' ago' : 'just now';
    return "hello"

@app.route('/<name>/<message>', methods=['POST'])
def show(name,message):
    com = mongo.db.comments
    print(list(com.find()))
    uid = com.insert({"name":name,"message":message})
    print(uid)
    req = request.json
    print(req,name,message)
    output = list(com.find())
    return jsonify({"output": output})



if __name__ == "__main__":
    app.run(debug=True)
