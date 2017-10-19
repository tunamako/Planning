from pymongo import MongoClient
import threading
import socket
import json

def add_event(data):
	db.visits.insert_one(data)

	if not db.stations.find({"StationID": data["stationID"]}).count():
		db.stations.insert_one(
			{
				"StationID": data["stationID"],
				"VisitCount": 0,
				"Battery": data["battery"],
				"PathTaken":data["path"]
			}
		)

	db.stations.update_one(
		{"StationID": data["stationID"]},
		{
			"$inc": {"VisitCount": 1},
			"$set": {"Battery": data["battery"]},
			"$set": {"PathTaken": data["path"]}
		}
	)

	db.rfids.update_one(
		{"RFID": data["rfid"]},
		{
			"$inc": {"VisitCount": 1}
		}
	)

def restart_birdfeeder():
	#TODO: send data over lora to reset a birdfeeder
	return

def update_photog_rfids():
	#TODO: propagate newly photographed rfids to all birdfeeders
	return

def lora_listener():
	while True: 
		#TODO:
		#listen on LoRa
		#Store payload in data
		#Check if payload contains an image
			#update_photog_rfids()
		#add_event(data)
		continue

def website_listener():
	while True:
		conn, client_addr = sock.accept()
		data = json.loads(conn.recv(4096))
		conn.close()

		if data["command"] == "restart":
			restart_birdfeeder()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8125))
sock.listen()

mongo_client = MongoClient("euclid.nmu.edu", 27017, username="admin", password="nmuchickadee", authSource="chickadees")
db = mongo_client.chickadees

threading.Thread(target=lora_listener).start()

website_listener()
