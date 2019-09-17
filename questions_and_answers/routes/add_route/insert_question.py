#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar
#from database.schemas.catalogo import Catalogo
from flask_mail import Message,Mail
from app.models.mcategorias import mCategoria

from passlib.hash import pbkdf2_sha256 as sha256

mail = Mail(app)
import json
from secrets import token_urlsafe
#Importando el conector odbc para las conexiones con mssql
import pyodbc
import datetime
#clase para el control de rutas en usuarios 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=190.85.232.78;DATABASE=DBKiero_Productos;UID=sa;PWD=S3rv3r1-27!')
from datetime import date

today = date.today()
get_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class insert(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
        
    def post(self):
                   
        try:
            data = request.get_json(force=True)
            questions = data['questions']
            id_Estado = 1
            id_Usuario= data['id_Usuario']
            Producto_id=data['Producto_id']
            
        except Exception as err:
            return {'status':'success','result':{'code':0,'message':'envie los parametros correspondientes'}}
        
        
        try:
            with conn:
                query = """
                insert into preguntas_kiero (fecha_Creacion,descripcion_Pregunta,id_Estado,id_Usuario,Producto_id) 
                VALUES ('{fecha_Creacion}','{descripcion_Pregunta}',{id_Estado},{id_Usuario},{Producto_id})""".format(fecha_Creacion=get_today,descripcion_Pregunta=questions,id_Estado=id_Estado,id_Usuario=id_Usuario,Producto_id=Producto_id)
                crsr = conn.execute(query)
                crsr.fast_executemany = True
        
                buildJSON = {"code":1,"message":"Pregunta creada satisfactoriamente"}
                __return = response(json.dumps({"status":"success",'result':buildJSON }),status=200, mimetype='application/json') 
                __return.headers['Access-Control-Allow-Origin'] = '*'
                __return.headers['Access-Control-Allow-Methods'] = 'POST'
                __return.headers['Allow'] = 'POST'

                return __return

        except Exception as px:
            print(px)
            json_response = {'code':0,'message':'problema interno'}
            __return = response({'status':'error','result':json_response},status=400, mimetype='application/json') 
            __return.headers['Access-Control-Allow-Origin'] = '*'
            __return.headers['Access-Control-Allow-Methods'] = 'POST'
            __return.headers['Allow'] = 'POST'
            return __return
 
