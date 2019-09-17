#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar
#from database.schemas.catalogo import Catalogo

from app.models.mcategorias import mCategoria
from app.services.scategorias import sCategorias

import json

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
# from app.services.connect_to_mysql import mysql


class get_categorias(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
        
    def post(self):

        data = request.get_json(force=True)

        categoria_id = data['categoria_id']
        
        scategorias = sCategorias(categoria_id=categoria_id) # se llaman a los servicios
        
        try:
            retorno = scategorias.SP_GET_CATEGORIES() # Se obtienen las categorias.
            # category_Tree = self.__Generar_Arbol_Categorias(retorno) # se asocian las categorias y se convierten a un json.
            #Se define el metodo del retorno response
            objectoJson = {'Mensaje':None,'Resultados':[]}
            if (categoria_id is not None):
                objectoJson['Mensaje'] =  'Proceso exitoso'
                objectoJson['Resultados'] = retorno
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
 