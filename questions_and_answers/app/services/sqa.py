#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
#   Operaciones SQL  con categorias
class sQuestions_and_answers: 
    #   constructor
    def __init__(self,usuario_id=None):
        self.__usuario_id = usuario_id
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        #self.__constring = connectionString().connectionODBC() #    Conexion a la base de datos.
        pass

    #   Trae todas las categorias del productos 
    def GET_ALL_QA (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "select Usuario_id,Documento,Nombres,Apellidos,Direccion,Email  from tbl_Usuarios where Usuario_id = {usuario}".format(usuario=self.__usuario_id)
            cursor.execute(sentencia)
            resultado = cursor.fetchone()
        #   Se recorre los resultados y se guardan el un array
        return resultado
    