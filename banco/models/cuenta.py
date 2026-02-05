from .cliente import Cliente
from .cuenta_ahorros import CuentaAhorro
from .cuenta_corriente import CuentaCorriente
from .cdt import Cdt

class Cuenta:
    def __init__(self, id):
        self.__id = id
        self.__cliente = Cliente
        self.__CCoriente = CuentaCorriente
        self.__CAhorro = CuentaAhorro
        self.cdts = []

    def saldo_total(self):
        total = self.__CCoriente.saldo + self.__CAhorro.saldo
        
        for cdt in self.cdts:
            total += cdt.saldo_actual
        return total
