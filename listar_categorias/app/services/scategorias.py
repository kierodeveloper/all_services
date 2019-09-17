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
    def GET_CATEGORIES(self,id):
        try: 
            conn_mongo = pymongo.MongoClient(self.__constring)
        except: 
            print("Could not connect to MongoDB") 
        db = conn_mongo.kiero
        collection = db.category
        cursor = collection.find({"parent_id":int(id),},{"_id":False,"parent_id":False})
        return cursor

        