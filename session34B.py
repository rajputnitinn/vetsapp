from session34 import Customer
from session34A import MongoDBHelper
from bson.objectid import ObjectId


def main():

    db = MongoDBHelper()

    #customer = Customer()
    #customer.read_customer_data()

    #document = vars(customer)

    #db.insert(document)

    #query = {'phone': '+91 7707942744'}
    query = {'_id': ObjectId('64c35b9b77d090171767162d')}
    # db.delete(query)

    #db.fetch()
    db.fetch(query= query)
    document_data_to_update = { 'name':' Nitin kumar','age': 21 }
    db.update(document_data_to_update,query)


if __name__ == "__main__":
    main()



    

