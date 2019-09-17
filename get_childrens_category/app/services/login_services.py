import pyodbc
from app.controller.connectionString import return_conection_string
#from core.http_controller.globals_controller.security.login import authenticate,identity
# En esta clase se hacen los servicios (Op sql) relacionados  con la tabla catalogo

class start_login:
    def __init__(self,email=None,password=None):
        self.__email = email
        self.__password = password
        self.__constring = return_conection_string(argument='mssql', db_database='NUCLEO_DE_USUARIOS')
        pass
 
    def SP_LOGIN(self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=1000) #Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            cursor.execute("EXEC SP_LOGIN_USERS @email='{0}',@password='{1}'"
            .format(self.__email,self.__password))
            resultado = cursor.fetchone()

        return resultado

