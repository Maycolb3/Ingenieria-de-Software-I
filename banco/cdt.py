
class Cdt:
    def __init__(self, id_cdt, monto_inicial, interes_mensual):
        self.__id = id_cdt
        self.__monto_inicial = monto_inicial
        self.__interes_mensual = interes_mensual

    def avanzar_mes(self):
        self.__meses_transcurridos += 1

    def calcular_interes(self):
        interes = self.__monto_inicial * self.__interes_mensual
        self.__monto_inicial += interes
        return interes

    @property
    def saldo(self):
        return self.__monto_inicial

    
