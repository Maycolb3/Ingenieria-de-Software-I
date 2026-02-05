
class CuentaCorriente:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return True
            #print(f"Monto ingresado '{monto}'.")

    def retirar(self, monto):
        if monto > 0 and monto < self.__saldo:
            self.__saldo -= monto
            return True
        else:
            return False
            #print("Monto incorrecto.")