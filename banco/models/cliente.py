
class Cliente:
    def __init__(self,cedula,nombre):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__cuenta = None

    def nombre(self):
        return self.__nombre 
    
    def cedula(self):
        return self.__cedula
    
    