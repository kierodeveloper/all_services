#   Clase Usuarios Rutas

#   Creada por: ...

#   Fecha creacion: ...



#Archivos necesarios para flask



#Se llama el objeto de flask

from flask import jsonify, request

from routes.router import app,resource,response,req,reqpar

#from database.schemas.catalogo import Catalogo



from app.models.mcategorias import mCategoria

from app.services.sperfil_usuario import sGet_Data_Usuario



import json

from json import dumps

#Importando el conector odbc para las conexiones con mssql

import pyodbc

#clase para el control de rutas en usuarios 

# from app.services.connect_to_mysql import mysql





class get_usuario(resource):

    def __init__(self):

        #   Se aniaden los parametros que se van a utilizar

        self.__parser = reqpar.RequestParser()

        self.__parser.add_argument('id', type=str,required=True,help='Id del usuario')

        pass



    def _generate_json_usuario(self,retorno,usuario_id):

        try:

            id = retorno[0]

            name = retorno[1]

            lastname = retorno[2]

            nickname = retorno[3]

            document_id = retorno[4]

            number_phone = retorno[5]

            email = retorno[6]

            email_status = retorno[7]

            status = retorno[8]

        except Exception as err:

            print('data_perfil ' + str(err) )

#========================================================================        

        get_addresses = sGet_Data_Usuario(usuario_id).SP_GET_ADDRESSES()

#========================================================================

        try:

            buildJSON_addresses = [{

                "name_and_lastname":data.name_and_lastname,

                "department":data.department,

                "city":data.city,

                "neighborhood":data.neighborhood,

                "via":data.via,

                "number_via":data.number_via,

                "additional_data":data.additional_data,

                "number_contact":data.number_contact

            }for data in get_addresses]

        except Exception as err:

            print(err)

        try:

            body_json_perfil_without_address={

                

                "name":name,

                "lastname":lastname,

                "nickname":nickname,

                "document_id":document_id,

                "number_phone":number_phone,

                "email":email,

                "email_status":email_status if int(email_status) == 1 else "email no confirmado",

                "status": status if int(status) == 1 else "usuario sin servicio",

                "addresses":None

                }

            body_json_perfil_without_address['addresses'] = buildJSON_addresses

            return(body_json_perfil_without_address)

        except Exception as err:

            print ("err > "+str(err))

        

    def get(self):

        args = self.__parser.parse_args()

        usuario_id = args['id']

        s_usuario = sGet_Data_Usuario(usuario_id=usuario_id) # se llaman a los servicios

        try:

            retorno = s_usuario.SP_GET_USUARIOS() # Se obtienen las categorias.

            #Se define el metodo del retorno response

            if (retorno is not None):

                buildJSON = self._generate_json_usuario(retorno,usuario_id)

                __return = response(json.dumps({"status":"success",'result':buildJSON }),status=200, mimetype='application/json') 

                __return.headers['Access-Control-Allow-Origin'] = '*'

                __return.headers['Access-Control-Allow-Methods'] = 'POST'

                __return.headers['Allow'] = 'POST'

                return __return

            else:

                __return = response(json.dumps({"status":"error",'result': 'usuario no encontrado'}),status=400, mimetype='application/json') 

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

 
