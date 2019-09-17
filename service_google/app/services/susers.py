
import pyodbc
from app.controller.connectionString import return_conection_string
#   Operaciones SQL  con Productos

class users:
    #   constructor
    def __init__(self):
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass

    #   Trae todas los productos dependiendo del id
    def INSERT_USER(self,name,lastname,email,idGoogle,email_status,status,nickname):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=6) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "insert into users (name,lastname,email,idGoogle,email_status, status,nickname) Values ('{name}','{lastname}','{email}','{idGoogle}','{email_status}','{status}','{nickname}')".format(name=name,lastname=lastname,email=email,idGoogle=idGoogle,email_status=email_status, status=status,nickname=nickname)
            cursor.execute(sentencia)
        #   Se recorre los resultados y se se retornan
        
    def VALIDATE_USER(self,email):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=6) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "select email from users where email = '{email}'".format(email=email)
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        return resultado
        #   Se recorre los resultados y se se retornan
        