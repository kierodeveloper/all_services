#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar
#from database.schemas.catalogo import Catalogo
import json,re
import html2text
import string
from app.services.susers import users

import json

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
# from app.services.connect_to_mysql import mysql

 
class get_campaing(resource):
    #   contructor
    
    def _build_json(self,rows):
        array = []
        for row in rows:
            _json = {
                'id':row[0],
                'campaing_name':row[1],
                'url_image':row[2],
                'link_capaing':row[3],

            }
            array.append(_json)
        return array
  

        
    def post(self):
        data = request.get_json()
        try:
            name = data['name']
            lastname = data['lastname']
            email = data['email'] 
            idGoogle = data['idGoogle']
            email_status = 0
            status = 1
            nickname = data['nickname']
        except Exception:
            return "Envie todos los datos correctamente"

        try:

            retorno2 = users().VALIDATE_USER(email=email)

            if retorno2:
                print("usuario registrado")
                return "usuario registrado"
            
            retorno = users().INSERT_USER(name=name,lastname=lastname, email=email,idGoogle=idGoogle,email_status=email_status,status=status,nickname=nickname)

            objectoJson = {}
            objectoJson['Mensaje'] =  'Proceso exitoso'
            objectoJson['Resultados'] = str(retorno)
            _json = json.dumps(objectoJson)
            _response = response(_json,status=200, mimetype='application/json')
            _response.headers['Access-Control-Allow-Origin'] = '*'

            return _response

        except Exception as err:
            print(err)
    
