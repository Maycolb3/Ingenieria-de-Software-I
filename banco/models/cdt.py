
class Cdt:
    def __init__(self, id, monto_inicial, interes_mensual, meses_transcurridos):
        self.__id = id
        self.__monto_inicial = monto_inicial
        self.__interes_mensual = interes_mensual
        self.__meses_transcurridos = 0

    def avanzar_mes(self):
        self.__meses_transcurridos += 1

    @property
    def saldo_actual(self):
        return (self.__monto_inicial + ((self.__monto_inicial * self.__interes_mensual) * self.__meses_transcurridos))

    
