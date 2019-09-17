#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string

#   Operaciones SQL  con categorias
class sProducts_relationates: 
    #   constructor
    def __init__(self,values=None,category_id=None):
        self.__category_id = category_id
        self.__values = values
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass

    #   Trae todas las categorias del productos 
    def SP_GET_PRODUCT_RELATIONATES (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = []
        columns = None
        with conexion:     
            sentencia = "EXEC GET_PRODUCTS_BY_KEYWORDS @values='{values}', @category={category_id}".format(values = self.__values,category_id=self.__category_id)
            cursor.execute(sentencia)
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                resultado.append(dict(zip(columns, row)))
        #   Se recorre los resultados y se guardan el un array
        print(sentencia)
        return resultado
    