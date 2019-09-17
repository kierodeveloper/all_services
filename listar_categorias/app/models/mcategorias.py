

#   Clases de validaciones para las categorias.
class mCategoria:

    #   Constructor
    def __init__(self):
        #Inicializamos los atributos del la clase
        self.__id_Categoria = None
        self.__nombre_Categoria = None
        self.__categoria_Padre = None
        
    
    #   Atributos de la clase

    #   Id de categoria 
    @property
    def id_Categoria(self):
        return self.__id_Categoria
    @id_Categoria.setter
    def id_Categoria(self,value):
        if value.isDigit() == False:
            raise ValueError('El campo id categoria no es valido')
        if value is None:
            raise ValueError('El campo id categoria esta vacio')
        if int(value) == 0 :
            raise ValueError('El campo id categoria no es valido')
        self.__id_Categoria = value
    
    #   Nombre de categoria 
    @property
    def nombre_Categoria(self):
        return self.__nombre_Categoria
    @nombre_Categoria.setter
    def nombre_Categoria(self,value):
        if value is None or len(value) == 0:
            raise ValueError('El campo nombre categoria esta vacio')
        if len(value) > 25 :
            raise ValueError('El campo nombre categoria supera el limite de caracteres')
        self.__nombre_Categoria = value
    
    #   Categoria padre

    @property
    def categoria_Padre(self):
        return self.__categoria_Padre
    @categoria_Padre.setter
    def categoria_Padre(self,value):
        if value.isDigit() == False:
            raise ValueError('El campo categoria padre no es valido')
        if value is None or len(value) == 0:
            raise ValueError('El campo categoria padre esta vacio')
        if int(value) == 0 :
            raise ValueError('El campo categoria padre no es valido')
        self.__categoria_Padre = value