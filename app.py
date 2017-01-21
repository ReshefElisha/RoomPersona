
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def home():
	mongo.db.users.insert({'id':"0000000000", 'online':True})
	online_users = list(mongo.db.users.find({'online':True}))
	#return jsonify([d for d in online_users])
	return json.dumps(online_users, default=json_util.default)

if __name__ == "__main__":
	app.run()
