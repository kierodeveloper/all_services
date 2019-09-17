#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
#   Operaciones SQL  con categorias
class sGet_Data_Usuario: 
    #   constructor
    def __init__(self,usuario_id=None):
        self.__usuario_id = usuario_id
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        #self.__constring = connectionString().connectionODBC() #    Conexion a la base de datos.
        pass

    #   Trae todas las categorias del productos 
    def SP_GET_USUARIOS (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = """
            select id,name,lastname,nickname,document_id,number_phone,email,email_status,status
            from users
            where id = {usuario} or idGoogle = '{usuario}'
            """.format(usuario=self.__usuario_id)
            cursor.execute(sentencia)
            resultado = cursor.fetchone()
        #   Se recorre los resultados y se guardan el un array
        return resultado
    
    def SP_GET_ADDRESSES (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "EXEC SP_GET_ADDRESSES_USERS_KIERO @id_user = {usuario}".format(usuario=self.__usuario_id)
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        #   Se recorre los resultados y se guardan el un array
        return resultado
