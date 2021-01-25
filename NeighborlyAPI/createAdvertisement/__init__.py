import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://mongodb-neighborly-01:Hj149fALbvQfuyhz3t74nJZ5BHIbIHrRdE4gBcdQvYF6i5aAS2lUI7qRA7TBGtHEyVFZImv9Kq00zWRl5VQFSQ==@mongodb-neighborly-01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@mongodb-neighborly-01@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['db-udacity-neighborly-01']
            collection = database['ads']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )