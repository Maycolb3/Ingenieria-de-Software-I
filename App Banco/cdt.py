
class Cdt:
    def __init__(self, id_cdt, monto_inicial, interes_mensual):
        self.__id = id_cdt
        self.__monto_inicial = monto_inicial
        self.__interes_mensual = interes_mensual
        self.__meses_transcurridos = 0  

    def avanzar_mes(self):
        self.__meses_transcurridos += 1

    def calcular_interes(self):
        interes = self.__monto_inicial * self.__interes_mensual
        self.__monto_inicial += interes
        return interes

    @property
    def saldo(self):
        return self.__monto_inicial
    
    @property
    def id(self):
        return self.__id
    
    @property
    def tasa_interes(self):
        return self.__interes_mensual
    
    @property
    def meses_transcurridos(self):
        return self.__meses_transcurridos