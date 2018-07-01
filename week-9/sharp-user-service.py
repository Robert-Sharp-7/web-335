from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name":"Oscar",
    "last_name":"Martinez",
    "email":"omartinez@dunder-mifflin.net",
    "employee_id":"6666666",
    "date_created":datetime.datetime.utcnow()
    }

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id":"6666666"}))

from pymongo import MongoClient

import pprint

client = MongoClient('localhost',27017)

db = client.web335

employee_id = "2222222"

pprint.pprint(db.users.find_one({"employee_id":employee_id}))