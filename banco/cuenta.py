from .cuenta_ahorros import CuentaAhorro
from .cuenta_corriente import CuentaCorriente
from .cdt import Cdt

class Cuenta:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__CCoriente = CuentaCorriente()
        self.__CAhorro = CuentaAhorro()
        self.cdts = {}
        self.siguiente_id = 1
        self.mes_actual = 0
        
    @property
    def saldo_total(self):
        total = self.__CCoriente.saldo + self.__CAhorro.saldo
        
        for cdt in self.cdts.values():
            total += cdt.saldo
        return total
    
    def abrir_cdt(self, monto, tasa_interes, CAhorros=True):
        cuenta = self.__CAhorro if CAhorros else self.__CCoriente

        if cuenta.retirar(monto):
            id_cdt = self.siguiente_id
            nuevo_cdt = Cdt(id_cdt, monto, tasa_interes)
            self.cdts[id_cdt] = nuevo_cdt
            self.siguiente_id += 1
            return id_cdt
        return None
    
    def cerrar_cdt(self, id_cdt):
        if id_cdt in self.cdts:
            cdt = self.cdts[id_cdt]
            monto_transferir = cdt.saldo

            if self.__CCoriente.saldo >= 0:
                self.__CCoriente.depositar(monto_transferir)
            else:
                self.__CAhorro.depositar(monto_transferir)

            del self.cdts[id_cdt]
            return monto_transferir
        return None
    

    def get_cdt(self, id_cdt):
        return self.cdts.get(id_cdt)
    

    def get_todos_cdts(self):
        return list(self.cdts.values())
    

    def avanzar_mes(self):
        """Avanza un mes en el tiempo y calcula intereses"""
        self.mes_actual += 1
        
        # Calcular intereses
        interes_ahorro = self.__CAhorro.calcular_interes
        
        intereses_cdts = {}
        for id_cdt, cdt in self.cdts.items():
            interes = cdt.calcular_interes
            intereses_cdts[id_cdt] = interes
        
        return {
            'mes': self.mes_actual,
            'interes_ahorro': interes_ahorro,
            'intereses_cdts': intereses_cdts,
            'saldo_total': self.saldo_total
        }

        

    
    
