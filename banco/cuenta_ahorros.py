
class CuentaAhorro:
    def __init__(self,saldo_inicial):
        self.__saldo = saldo_inicial
        self.interes = 0.006

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self,monto):
        if monto > 0:
            self.__saldo += monto
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False
    
    @property
    def calcular_interes(self):
        interes_calculado = self.__saldo * self.interes
        self.__saldo -= interes_calculado
        return interes_calculado

