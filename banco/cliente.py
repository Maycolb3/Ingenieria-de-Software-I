
class Cliente:
    def __init__(self,cedula,nombre):
        self.__cedula = cedula
        self.__nombre = nombre

    def nombre(self):
        return self.__nombre 
    
    @property
    def cedula(self):
        return self.__cedula
    
    
    