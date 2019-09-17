#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc
import json 
from json import dumps
import re

# conn_str = (
#     "DRIVER={PostgreSQL Unicode};"
#     "DATABASE=other;"
#     "UID=odoo;"
#     "PWD=odoo;"
#     "SERVER=172.17.0.2;"
#     "PORT=5432;"
#     )
# conn = pyodbc.connect(conn_str)


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=204.141.52.148;DATABASE=DBKiero_Productos;UID=MachineBaseConnect3651;PWD=H1#KotS(xh5nF+tGv')

#usted ejecuta y me envia imagenes
with conn:
    query = """
SELECT
	productos.Titulo
from
	category categoria
inner join tbl_Productos productos on
	categoria.id = productos.Categoria_id
where
	parent_id = 49854
UNION SELECT
	p.Titulo
FROM
	tbl_Productos p
WHERE
	Categoria_id = 49854
    
    """
    crsr = conn.execute(query)
    rows = crsr.fetchall()
    # result = re.findall(r'\u00ed',str(rows))
    # print(result)

for row in rows:
    print(row)