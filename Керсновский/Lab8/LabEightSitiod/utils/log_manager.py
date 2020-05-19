import pymongo
from datetime import datetime

def create_log(ip, address):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['sitiod']
    table = db["logs"]

    log = {"client": ip,
            "time": datetime.now(),
            "request": address}
    table.insert_one(log)