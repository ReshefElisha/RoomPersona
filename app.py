
from flask import Flask, jsonify
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/init/')
def home():
	mongo.db.patrons.remove({'id':"*"})
	#if(list(mongo.db.patrons.find()).__len__() == 0):
	mongo.db.patrons.insert({
"id":"027984480", 
"environments":[
	{
		"name": "Meredith",
		"devices": [
			{
				"name": "Speaker",
				"settings": [
					{
						"settingName":"Song",
						"settingValue": "https://youtu.be/EV3NpQpjLDY"
					}
				]
			},
			{
				"name": "Monitor",
				"settings": [
					{
						"settingName": "Website",
						"settingValue": "http://tumblr.com"
					}
				]
			},
			{
				"name": "Monitor2",
				"settings": [
					{
						"settingName": "Background",
						"settingValue": "/home/pi/Pictures/paulaBG.jpg"
					}
				]
			},
			{
				"name": "Thermostat",
				"settings": [
					{
						"settingName": "Temperature",
						"settingValue":	"78"
					}
				]
			}
		]
	}
]})
mongo.db.patrons.insert({
"id": "027209470",
"environments": [
	{
		"name": "CaryQuad",
		"devices": [
			{
				"name": "Speaker",
				"settings": [
					{
						"settingName": "Song",
						"settingValue": "http://youtu.be/OzOpQ6VqHCo"
					}
				]
			},
			{
				"name": "Monitor",
				"settings": [
					{
						"settingName":	"Website",
						"settingValue": "http://www.amazon.com"
					}
				]
			},
			{
				"name": "Monitor2",
				"settings": [
					{
						"settingName": "Background"
						"settingValue":	"/home/pi/Pictures/jacksonBG/jpg"
					}
				]
			},
			{
				"name": "Thermostat",
				"settings": [
					{
						"settingName":	"Temperature",
						"settingValue":	"63"
					}
				]
			}
		]
	}
]})
mongo.db.patrons.insert({
"id": "029384719",
"environments": [
	{
		"name": "Wiley",
		"devices": [
			{
				"name": "Speaker",
				"settings": [
					{
						"settingName": "Song",
						"settingValue": "https://youtu.be/9E6b3swbnWg"
					}
				]
			},
			{
				"name": "Monitor",
				"settings": [
					{
						"settingName": "Website",
						"settingValue": "https://www.reddit.com"
					}
				]
			},
			{
				"name": "Monitor2",
				"settings" [
					{
						"settingName": "Background",
						"settingValue":	"/home/pi/Pictures/reshefBG.jpg"
					}
				]
			},
			{
				"name": "Thermostat",
				"settings" [
					{
						"settingName": "Temperature",
						"settingValue": "46"
					}
				]
			}
		]
	}
]})
	online_users = list(mongo.db.patrons.find())
	return json.dumps(online_users, default=json_util.default)
	
@app.route('/patron/<patid>')
def get_patron_json(patid):
	print patid
	#print list(mongo.db.patrons.find({"id":"029384719"}))
	return json.dumps(list(mongo.db.patrons.find({"id":patid})), default=json_util.default)

@app.route('/createpatron/<patid>')
def create_patron(patid):
	mongo.db.patrons.insert({'id':patid})
	return json.dumps(list(mongo.db.patrons.find({'id':patid})), default=json_util.default)
	
@app.route('/addprop/<patid>/environment/<envname>')
def add_env(patid, envname):
	patron = list(mongo.db.patrons.find({"_id":{'id':patid}}))[0]
	

if __name__ == "__main__":
	app.run(host='0.0.0.0')
