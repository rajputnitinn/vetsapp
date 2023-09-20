import pymongo
uri  = "mongodb+srv://nkrajput919:nitin@cluster0.kltsphs.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['python']
collections = db.list_collection_names()
for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)




