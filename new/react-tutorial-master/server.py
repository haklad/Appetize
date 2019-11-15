
import json
import os
import time
from flask import Flask, Response, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

app.config['MONGO_DBNAME'] = 'food'
app.config['MONGO_URI'] = "mongodb://localhost/food"
CORS(app)
mongo = PyMongo(app)

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    com = mongo.db.comments
    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        print(new_comment)
        uid = com.insert({"id":new_comment['id'],"name":new_comment['author'],"message":new_comment['text']})

    docs_list = list(com.find())
    output=[]
    for i in docs_list:
        print(i)
        output.append({"id": i['id'],"author":i['name'],"text":i['message']})

    return Response(
        json.dumps(output),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods':'*'
        }
    )

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)
