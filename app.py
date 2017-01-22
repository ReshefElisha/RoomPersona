
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
mongo = PyMongo(app)

mongo.db.users.insert({'id':"0000000000", 'online':True})

@app.route('/')
def home():
	mongo.db.users.insert({'id':"0000000000", 'online':True})
	online_users = list(mongo.db.users.find({'online':True}))
	#return jsonify([d for d in online_users])
	return json.dumps(online_users, default=json_util.default)
	
@app.route('/patron/<patid>')
def get_patron_json(patid):
	json.dumps(list(mongo.db.patrons.find({'id':patid})))
	
@app.route('/createpatron/<patid>')
def create_patron(patid):
	mongo.db.patrons.insert({'id':patid})
	return json.dumps(list(mongo.db.patrons.find({'id':patid})), default=json_util.default)
	
@app.route('/addprop/<patid>/environment/<envname>')
def add_env(patid, envname):
	patron = list(mongo.db.patrons.find({'id':patid}))[0]
	patron.
	

if __name__ == "__main__":
	app.run()
