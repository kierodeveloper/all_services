#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string

#   Operaciones SQL  con categorias
class sRandom_Products: 
    #   constructor
    def __init__(self):
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass

    #   Trae todas las categorias del productos 
    def BRING_RANDOM_PRODUCTS_BY_CATEGORIES (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = []
        columns = None
        with conexion:     
            sentencia = "EXEC BRING_RANDOM_PRODUCTS_BY_CATEGORIES"
            cursor.execute(sentencia)
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                resultado.append(dict(zip(columns, row)))
        #   Se recorre los resultados y se guardan el un array
        return resultado
    