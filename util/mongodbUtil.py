import pymongo


def insert(data):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['zyInfo']
    collection = db['majors']
    find_result = collection.find_one(data)
    if find_result is None:
        result = collection.insert_one(data)
    else:
        return 'DB had record'
    return result
    # return findresult

def get_majors() :
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['zyInfo']
    collection = db['majors']
    result = collection.find()
