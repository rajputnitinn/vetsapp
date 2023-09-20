import pymongo

class MongoDBHelper:
    def __init__(self, collection='user'):
        uri = "mongodb+srv://nkrajput919:nitin@cluster0.kltsphs.mongodb.net/?retryWrites=true&w=majority"

        client = pymongo.MongoClient(uri)
        self.db = client['Nitin']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document Inserted:", result)
        return result

    def delete(self, query):
        result = self.collection.delete_one(query)
        print("Document Deleted:", result)

    def fetch(self, query=""):
        documents = self.collection.find(query)
        return list(documents)

    def update(self, document, query):
        update_query = {'$set': document}
        result = self.collection.update_one(query, update_query)
        print("Updated Document:", result.modified_count)

    # Add a method to update the schema
    def update_schema(self):
        new_fields = {
            'income': 0.0,  # Set a default value for income
            'housing_status': '',  # Set a default value for housing_status
        }
        update_query = {'$set': new_fields}
        self.collection.update_many({}, update_query)
        print("Schema Updated for Collection:", self.collection.name)

# Usage example
if __name__ == "__main__":
    db_helper = MongoDBHelper(collection="user")
    db_helper.update_schema()
