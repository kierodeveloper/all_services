#   Clase Usuarios Rutas

#   Creada por: ...

#   Fecha creacion: ...



#Archivos necesarios para flask



#Se llama el objeto de flask

from elasticsearch import Elasticsearch

from flask import jsonify, request

from routes.router import app,resource,response,req,reqpar

#from database.schemas.catalogo import Catalogo



from app.services.sproducts_relationates import sProducts_relationates



import json

import os

from json import dumps



#Importando el conector odbc para las conexiones con mssql

#import pyodbc

#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=204.141.52.148;DATABASE=DBKiero_Productos;UID=MachineBaseConnect3651;PWD=H1#KotS(xh5nF+tGv')



#importamos hunspell para agregar palabras de diminutivos y este tambien nos sirve para palabras que elastic search





#clase para el control de rutas en usuarios 

# from app.services.connect_to_mysql import mysql

class rSearch(resource):

    

    def _connect_elasticsearch(self):

        _es = None

        _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

        if _es.ping():

            return(_es)

        else:

            return('Awww it could not connect!')

        return _es



    def _search_categorys(self,correction):

        return_json = []

        _es = self._connect_elasticsearch()

        res= _es.search(index='categorias', body={

                "query":{

                    "match":{

                        "name": correction

                    }

                },

                "sort":[

                    "_score"

                ]

            },size=10)

        for row in res['hits']['hits']:

            build_json = {

                'id' : row['_source']['id'],

                'name' : row['_source']['name'],

                'linkcategory' : 'https://listado.kiero.co/listcategory/?id-'+ row['_source']['id']+'/#'+(self._replaceMultiple(row['_source']['name'],["[","!","@","#",'"',"$",";","]","'",'(',')','/','?',',','.'],'')).replace(' ','%20')

            }

            return_json.append(build_json)

        return return_json

    

    def _search_products_with_category(self,category_id, query):

        #print('category')

        _es = self._connect_elasticsearch()

        res= _es.search(index='productos',body={

        'query':{

            'bool':{

                'must':{

                    'match':{

                        'Titulo':query

                    }

                    },

                    "filter":{

                        "range":{

                            "Category_id":{

                                "gt":category_id

                            }

                        }

                    }

                }

            }

        })



        return( res['hits']['hits'])



    def _replaceMultiple(self,mainString, toBeReplaces, newString):

        # Iterate over the strings to be replaced

        for elem in toBeReplaces :

            # Check if string is in the main string

            if elem in mainString :

                # Replace the string

                mainString = mainString.replace(elem, newString)

        

        return  mainString



    def _suggestWords(self,query):

        ite = True;

        word = []

        correction = ''

        resultado= True;

        

        while ite:

            es = self._connect_elasticsearch()

            res= es.search(index='productos',body={

                    "suggest": {

                        "text" : query,

                        "my-suggest-1" : {

                            "term" : {

                                "field" : "Titulo"

                            }

                        }

                    }

                })



            for i in res['suggest']['my-suggest-1']:

                if i['options']:

                    

                    correction += i['options'][0]['text'] + ' '

                else:

                    correction += i['text'] + ' '



            ite = False 

                 

        return (correction)



    def _search_products(self,query):

    

        correction = self._suggestWords(query)

        categoriiiiis = self._search_categorys(correction)

        _es = self._connect_elasticsearch()

        x = correction.split(' ')

        if len(x) > 2:

            res= _es.search(index='productos', body={

                "query":{

                    "match":{

                        "Fake": correction

                    }

                }

            },size=1000)

        else:

            res= _es.search(index='productos',body={

                "query":{

                    "match":{

                        "Fake": correction

                    }

                },

                "sort":[

                    {"Relevancia_cat.keyword":"asc"},

                    {"Relevancia_pro.keyword":"asc"}

                ]

            },size=1000)



        return_json = []

        for row in res['hits']['hits']:

            build_json = {

                'query': correction,

                'Producto_Id' : row['_source']['Producto_Id'],

                'Categoria_id' : row['_source']['Categoria_id'],

                'Titulo' : row['_source']['Titulo'],

                #'Estado' : row['_source']['Estado'],

                'permalink' : 'https://articulo.kiero.co/product-details/?id-'+ row['_source']['Producto_Id']+'-'+(self._replaceMultiple(row['_source']['Titulo'],["[","!","@","#",'"',"$",";","]","'",'(',')','/','?',',','.'],'')).replace(' ','-'),

                'Precio_cop' : row['_source']['Precio_cop'],

                'Imagenes_1' : row['_source']['Imagenes_1'],

                'Relevancia_cat' : row['_source']['Relevancia_cat'],

                'Relevancia_pro' : row['_source']['Relevancia_pro'],

            }

            return_json.append(build_json)

        return return_json,categoriiiiis



    def post(self):



        try:

            data = request.get_json(force=True)

            search_query=data['query']

                # category_id=data['category_id']

        except Exception as err:

            return {'status':'success','result':{'code':0,'message':'envie los parametros correspondientes'}}

            

        try:

                        

            if search_query:

                # retorno = self._search_products_with_category(category_id,search_query)

                retorno,categoriiiiis = self._search_products(search_query)                              

            elif len(search_query) > 0:

                retorno = self._search_products(search_query)

                

            

            __return = response(json.dumps({"status":1,'Total':len(retorno),'result':retorno,"Categorias_buscadas":categoriiiiis }),status=200, mimetype='application/json') 

            __return.headers['Access-Control-Allow-Origin'] = '*'

            __return.headers['Access-Control-Allow-Methods'] = 'POST'

            __return.headers['Allow'] = 'POST'

            return __return

        except Exception as err:

            print(err)

            objectoJson={}

            objectoJson['Mensaje'] =  'Hubo un error'

            objectoJson['Resultados'] = None

            _json = json.dumps(objectoJson)

            _response = response(_json,status=500, mimetype='application/json')

        

        _response.headers['Access-Control-Allow-Origin'] = '*'

        return _response



    def options(self):

        return {'Metodos permitidos' : ['GET'] }, 200, \

        { 'Access-Control-Allow-Origin': '*', \

        'Access-Control-Allow-Methods' : 'GET', \

        'Access-Control-Allow-Headers': 'X-Custom-Header'   }


