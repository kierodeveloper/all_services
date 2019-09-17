#Modulos relacionados con flask
from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api,reqparse
from flask_cors import CORS
import os
#Clases modulos
template_dir = os.path.abspath('public')
app = Flask(__name__, template_folder=template_dir)
#Configuraciones iniciales
Bootstrap(app)
api = Api(app)
resource = Resource
req = request
response = Response
reqpar = reqparse
cors = CORS(app, resources={r"/*": {"origins": "*","headers":"X-Custom-Header"}})
 
#Importando todas las clases de rutas y aniadendolas
from routes.add_route.rrandom_products import rRandom_Products

#       ----    RUTAS DEL PROYECTO  ----        #
#add-rutas

api.add_resource(rRandom_Products,'/rp') 
#       ----    FIN DE LAS RUTAS PROYECTO  ----        #
