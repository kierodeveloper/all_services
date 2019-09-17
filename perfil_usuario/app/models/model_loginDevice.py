import os
class mloginDevice:
    """"""
    #Constructor
    def __init__(self):
        self.__userDevice = None
        self.__idDevice = None
        pass
    
       #id propiedades
    """"""
    @property 
    def name(self):
        return (self.__userDevice)
    @name.setter
    def name(self,value):
        if value is None or len(value) == 0:
            raise ValueError('El campo esta vacio')
        self.__userDevice = value  