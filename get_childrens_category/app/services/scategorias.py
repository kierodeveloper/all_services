#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
#   Operaciones SQL  con categorias
class sCategorias: 
    #   constructor
    def __init__(self,nombre_Categoria=None,categoria_id=None):
        self.__nombre_Categoria = None
        self.__categoria_id = categoria_id
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        #self.__constring = connectionString().connectionODBC() #    Conexion a la base de datos.
        pass

    #   Trae todas las categorias del productos 
    def SP_GET_CATEGORIES (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "EXEC GET_CHILDRENS_CATEGORIES @id_Categoria = {categoria_id}".format(categoria_id=self.__categoria_id)
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        #   Se recorre los resultados y se guardan el un array
        array = [] #    El array de retorno 
        json = {        }
        for row in resultado:            
            json['id'] = row.id
            json['parent_path'] = row.parent_path  
            json['name'] = row.name
            json['complete_name'] = row.complete_name
            json['parent_id'] = row.parent_id if row.parent_id is None else print('si fallo')
            array.append(json)
            json = {} 
        return array
    
