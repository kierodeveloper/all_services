class NewRoute():
    def make_route(name_new_route):
        """Crear nueva ruta en la app"""
        import time 
        datatime = time.strftime("%c")
        a = None
        
        with open('routes/router.py','w') as f:
            f.writelines(a)
            f.close()
        new_route = open("routes/add_route/"+name_new_route+".py", "w")
        new_route.write("""    
#   Clase Usuarios Rutas
#   Creada por: Your_name
#   Fecha creacion: {0}

#Se llama el objeto de flask
from flask import jsonify, request,Flask, render_template
from routes.router import app,resource,response,req,reqpar
import json102

#se debe de añadir los modelos y los servicios que vendrian siendo los controladores y los ejecutores de las acciones en el codigo

from app.controller.connectionString import connection_Device

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 

#-----------------Bug de errores------------------------------#
#Aqui puedes predefinir el control de errores que tendran las respuestas de cada una de las validaciones
#example: name_variable = json.dumps(DATA JSON)

#data_retult_error = json.dumps()
#-----------------Fin de bug de errores------------------------------#

class {1}(resource):
    def __init__(self):
        pass
    def get(self):
        return ("method get")
    def post(self):
        return ("method post")
    def options(self):
        return ("method options")
        """.format(datatime,name_new_route))
        new_route.close()

