#   Clase Usuarios Rutas

#   Creada por: ...

#   Fecha creacion: ...



#Archivos necesarios para flask



#Se llama el objeto de flask

from flask import jsonify, request

from routes.router import app,resource,response,req,reqpar

from urllib.parse import urlparse



#from database.schemas.catalogo import Catalogo



from app.services.srandom_products import sRandom_Products



import json

import os



#Importando el conector odbc para las conexiones con mssql

import pymongo

#clase para el control de rutas en usuarios 

# from app.services.connect_to_mysql import mysql



class rRandom_Products(resource):

    def __init__(self):

        self.__conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

        self.__parser = reqpar.RequestParser()       

        self.__parser.add_argument('id', type=int,required=True,help='Envie el id del producto')

    



    def create(self, array):

        clear_data = []

        for row in array:

            imagen_W = ((urlparse(row['_L'])).path.rsplit('/', 1)[1]).splitlines()[0]

            build = {

                "Categoria_id": row['Categoria_id'],

                "Titulo": row['Titulo'],

                "Precio_cop": (row['Precio_cop']).split('.')[0],

                "Producto_id": row['Producto_Id'],

                "Imagen": row['_L'] if row['_L'] else row['Imagenes_1'],

                "Imagen_W": 'https://images.kiero.co/images/_W/'+(imagen_W).split('.')[0]+'.webp'

            }

            clear_data.append(build)

        return clear_data



    def get(self):



        # queryExec = sRandom_Products().BRING_RANDOM_PRODUCTS_BY_CATEGORIES()

        # print(queryExec[0])

        # rt = []

        objectoJson = {}

        db = self.__conn.kiero



        # Created or Switched to collection names



        collection = db.products_sliders_5 #products3





        db_category = self.__conn.public_categories

        collection_category = db_category.category

        try:

            random_category = collection.aggregate([{'$match': {'Categoria_id':{'$exists':True}}},{ "$sample": { "size": 1 }}])

            for category in random_category:

                category = (category['Categoria_id'])



            cursor = collection.aggregate([{'$match': {'Categoria_id':str(category)}},{ "$sample": { "size": 8 }}])

            random_products=[]

            for row in cursor:

                random_products.append(row)



            random_products = self.create(random_products)

            



            if random_products:

                

                buildJSON = {"code":1,"message":"productos encontrados satisfactoriamente",'random_products':random_products}

                __return = response(json.dumps({"status":"success",'result':buildJSON}),status=200, mimetype='application/json') 

                __return.headers['Access-Control-Allow-Origin'] = '*'

                __return.headers['Access-Control-Allow-Methods'] = 'POST'

                __return.headers['Allow'] = 'POST'

                return __return



            else:

                buildJSON = {"code":0,"message":"Algo salio mal"}

                __return = response(json.dumps({"status":"success",'result':buildJSON}),status=200, mimetype='application/json') 

                __return.headers['Access-Control-Allow-Origin'] = '*'

                __return.headers['Access-Control-Allow-Methods'] = 'POST'

                __return.headers['Allow'] = 'POST'

                return __return

            # for data in queryExec: 

            #     data['precio'] = str(data['precio'])

            #     data['imagenes_Productos'] = str(data['imagenes_Productos']).split('~^~')

            #     rt.append(data)



        except Exception as err:

            print(err)

            objectoJson['Mensaje'] =  'Hubo un error'

            objectoJson['Resultados'] = str(err)

            _json = json.dumps(objectoJson)

            _response = response(_json,status=500, mimetype='application/json')

        

            _response.headers['Access-Control-Allow-Origin'] = '*'

            return _response



    def options(self):

        return {'Metodos permitidos' : ['GET'] }, 200, \

        { 'Access-Control-Allow-Origin': '*', \

        'Access-Control-Allow-Methods' : 'GET', \

        'Access-Control-Allow-Headers': 'X-Custom-Header'   }


