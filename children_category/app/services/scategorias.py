import pyodbc
import pymongo
from app.controller.connectionString import return_conection_string

#   Operaciones SQL  con categorias
class sCategories: 
    #   constructor
    def __init__(self,values=None,category_id=None):
        self.__category_id = category_id
        self.__values = values
        self.__constring = return_conection_string(argument='mongo')
        pass

    #   Trae todas las categorias del productos 
    def GET_CATEGORIES(self):
        try: 
            conn_mongo = pymongo.MongoClient(self.__constring)
        except: 
            print("Could not connect to MongoDB") 

        db = conn_mongo.kiero
        collection = db.category
        #cursor = collection.find({"parent_id":None},{"_id":False,"path_from_root":False,"parent_id":False})
        cursor = collection.find({"parent_id":None,"name": { "$exists": True }},{"_id":False,"id":True,"name":True,"permalink":True,"childrens_categories":True}).sort([("name", 1)])

        return cursor

        
