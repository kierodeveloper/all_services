#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar
#from database.schemas.catalogo import Catalogo

from app.models.mcategorias import mCategoria
from app.services.scategorias import sCategories

import json

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
# from app.services.connect_to_mysql import mysql


class get_categorias(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        self.__parser = reqpar.RequestParser()
        self.__parser.add_argument('id', type=str,required=True,help='Id de la categoria')
        
    def get(self):

        scategorias = sCategories() # se llaman a los servicios
        args = self.__parser.parse_args()
        if 'id' not in args:
            return None,404
        try:
            retorno = scategorias.GET_CATEGORIES(args['id'])
             # Se obtienen las categorias.
            #Se define el metodo del retorno response
            array = []
            for row in retorno:
                array.append(row)
            objectoJson = {'Mensaje':None,'Resultados':[]}
            if (retorno is not None):
                objectoJson['Mensaje'] =  'Proceso exitoso'
                objectoJson['Resultados'] = array
                _json = json.dumps(objectoJson)
                _response = response(_json,status=200, mimetype='application/json')
                _response.headers['Access-Control-Allow-Origin'] = '*'
            else :
                objectoJson['Mensaje'] =  'Hubo un error' 
                _json = json.dumps(objectoJson)
                _response = response(_json,status=400, mimetype='application/json')
            return _response
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500 

    def options(self):
        return {'Metodos permitidos' : ['PUT','GET','POST'] }, 200, \
        { 'Access-Control-Allow-Origin': '*', \
        'Access-Control-Allow-Methods' : 'PUT,GET,POST', \
        'Access-Control-Allow-Headers': 'X-Custom-Header'   }
 