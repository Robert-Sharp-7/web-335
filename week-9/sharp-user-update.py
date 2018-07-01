import
    pymongo
    pprint
    datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    {"employee_id":"6666666"},
    {
        "$set":{
            "email":"rsharp@my.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id":"6666666"}))

db.users.find_one({"employee_id":6666666})