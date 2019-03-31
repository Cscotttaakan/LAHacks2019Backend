#load patients
from bson.objectid import ObjectId
import pymongo
import model_mongodb

import json


with open('patients.json') as json_file:
    patients = json.load(json_file)
    for val in patients:
        data = { val : patients[val] }
        model_mongodb.create(data)




