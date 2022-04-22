import os
import pymongo




def getRuleCollection():
    application_client = pymongo.MongoClient("mongodb://localhost:27017/databaseName?authSource=admin")
    application_db = application_client["ia_supplements_rules"]
    application_collection = application_db["rule"]
    return application_collection

def getSoldSupplementsCollection():
    application_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
    application_db = application_client["commerce_supplements"]
    application_collection = application_db["supplements_sold"]
    return application_collection


#print(list(getSoldSupplementsCollection().find()))


