import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://mongodb-neighborly-01:Hj149fALbvQfuyhz3t74nJZ5BHIbIHrRdE4gBcdQvYF6i5aAS2lUI7qRA7TBGtHEyVFZImv9Kq00zWRl5VQFSQ==@mongodb-neighborly-01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodb-neighborly-01@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['db-udacity-neighborly-01']
        collection = database['ads']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

