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
from app.services.sqa import sQuestions_and_answers
mail = Mail(app)
import json
from secrets import token_urlsafe
import datetime
#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=190.85.232.78;DATABASE=DBKiero_Productos;UID=sa;PWD=S3rv3r1-27!')
from datetime import date, time

today = date.today()
get_today = today.strftime("%d/%m/%Y")


class get_all_answers(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        self.__parser = reqpar.RequestParser()
        self.__parser.add_argument('id', type=str,required=True,help='Id del producto')
        pass
    
    def _build_qa(self,rows):
        buildJson = []
        buildJson = [{
                "pregunta":row[0],
                "respuesta":row[1],
                "tiempo_respuesta":str(row[2])
            } for row in rows]
        return(buildJson)
    def get(self):
                
        args = self.__parser.parse_args()
        Producto_id = args['id']
        with conn:
            query = """select descripcion_Pregunta,respuesta,fecha_respuesta from DBKiero_Productos.dbo.preguntas_kiero where Producto_id = {Producto_id}""".format(Producto_id=Producto_id)
            crsr = conn.execute(query)
            rows = crsr.fetchall()
            crsr.fast_executemany = True
        
        try:
            if rows:
                buildqa = self._build_qa(rows=rows)
                buildJSON = {"code":1,"message":buildqa}
                __return = response(json.dumps({"status":"success",'result':buildJSON }),status=200, mimetype='application/json') 
                __return.headers['Access-Control-Allow-Origin'] = '*'
                __return.headers['Access-Control-Allow-Methods'] = 'POST'
                __return.headers['Allow'] = 'POST'
                return __return
            else:
                obj_json = {"code":0,"message":"producto sin preguntas"}
                __return = response(json.dumps({"status":"success",'result':obj_json }),status=200, mimetype='application/json') 
                __return.headers['Access-Control-Allow-Origin'] = '*'
                __return.headers['Access-Control-Allow-Methods'] = 'POST'
                __return.headers['Allow'] = 'POST'
                return __return 


        except Exception as px:
            print(px)
            
            __return = response({'Error':'Hubo un error interno'},status=400, mimetype='application/json') 
            __return.headers['Access-Control-Allow-Origin'] = '*'
            __return.headers['Access-Control-Allow-Methods'] = 'POST'
            __return.headers['Allow'] = 'POST'
            return __return
 
