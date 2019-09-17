#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc
import json 
from json import dumps
import re

conn_str = (
    "DRIVER={PostgreSQL Unicode};"
    "DATABASE=other;"
    "UID=odoo;"
    "PWD=odoo;"
    "SERVER=172.17.0.2;"
    "PORT=5432;"
    )
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=204.141.52.148;DATABASE=DBKiero_Productos;UID=MachineBaseConnect3651;PWD=H1#KotS(xh5nF+tGv')

conn = pyodbc.connect(conn_str)

#usted ejecuta y me envia imagenes
with conn:
    query = """
    select * from product_public_category order by id
    """
    crsr = conn.execute(query)
    rows = crsr.fetchall()

array = [] #    El array de retorno 
json = {        }
# Entonces la vuelta es la siguiente, asi sacamos las padres.
# jsonpadres = [{"id":row.id,"parent_path":row.parent_path,"name":row.name,"complete_name":row.complete_name,"categorias_Hijas":None} for row in rows if row.parent_id is None]
#calma

#lo que pasa es que al parecer estaba consumiendo una base de datos que no es, quiero probar a ver como me trae las categorias si le dio


jsonpadres = [{
    "id":row.id,
    "parent_path":str(row.id) + ' /',
    "name":row.name,
    "complete_name":row.name + ' /',
    "categorias_Hijas":None
} for row in rows if row.parent_id is None]


i = 0
for jsnp in jsonpadres:  
    jsonhijas = [{
        "id":row.id,
        "parent_path":str(jsnp['id']) + ' / ' + str(row.id),
        "name":row.name,
        "complete_name": jsnp['name'] + ' / ' + row.name,
        "categorias_Hijas":None
    } for row in rows if row.parent_id == jsnp['id']]

    qwe = 0
    for nietasT in jsonhijas:  
        nietas = [{
            "id":row.id,
            "parent_path":str(jsnp['id']) + ' / ' + str(nietasT['id']) + ' / ' + str(row.id),
            "name":row.name,
            "complete_name":jsnp['name'] + ' / ' + nietasT['name'] + ' / ' + row.name,
            "categorias_Hijas":None
        } for row in rows if row.parent_id == nietasT['id']]
        
        jsonhijas[qwe]["categorias_Hijas"] = nietas
        qwe = qwe+1

    jsonpadres[i]["categorias_Hijas"] = jsonhijas
    i = i+1    #así es 
print(dumps(jsonpadres))