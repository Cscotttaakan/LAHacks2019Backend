from bson.objectid import ObjectId
from flask_pymongo import PyMongo

builtinlist_list = list

mongo = None

def _id(id):
    if not isinstance(id, ObjectId):
        return ObjectId(id)
    return id

def from_mongo(data):
    if not data:
        return None

    data['id'] = str(data['_id'])

def init_app(app):
    global mongo

    mongo = PyMongo(app)
    mongo.init_app(app)

def read(id):
    result = mongo.db.records.find_one({id : {'$exists': True}})
    return result

def create(data):
    result = mongo.db.records.insert_one(data)
    return read(result.inserted_id)

def update(data, id):
    mongo.db.records.replace_one({'_id': _id(id)}, data)
    return read(id)

def delete(id):
    mongo.db.records.delete_one({'_id': _id(id)})
