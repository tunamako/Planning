from pymongo import MongoClient


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



client = MongoClient("euclid.nmu.edu", 27017)
db = client.chickadees

#TODO:
#listen on LoRa
#Store payload in data
#Check if payload contains an image
	#If so, update list of photographed rfids for each birdfeeder

add_event(data)
