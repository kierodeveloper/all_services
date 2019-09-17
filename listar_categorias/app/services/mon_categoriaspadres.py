import pymongo

try: 
    conn_mongo = pymongo.MongoClient("mongodb://172.17.0.3:27017/")
    print("Connected successfully!!!") 
except: 
    print("Could not connect to MongoDB") 

db = conn_mongo.tbl_random_products
collection = db.products_by_category