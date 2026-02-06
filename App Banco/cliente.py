class Cliente:
    def __init__(self, cedula, nombre):
        self.__cedula = cedula
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre 
    
    @property
    def cedula(self):
        return self.__cedula
    
    def __str__(self):
        return f"{self.__nombre} (CC: {self.__cedula})"
    
