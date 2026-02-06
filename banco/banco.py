#Lógica
from .cliente import Cliente
from .cuenta import Cuenta

class Banco:
    
    def __init__(self):
        self.clientes = []
        self.cuentas = {}
        self.cliente_actual = None

    def registrar_cliente(self, cedula, nombre):
        
        if not cedula or not nombre:
            return False, "Cédula y nombre son requeridos"

        if cedula in self.cuentas:
            return False, f"Ya existe un cliente con cédula {cedula}"
        
        try:
            cliente = Cliente(cedula, nombre)
            cuenta = Cuenta(cliente)

            self.clientes.append(cliente)
            self.cuentas[cedula] = cuenta
            self.cliente_actual = cliente
            return True, "Cliente y cuenta creados exitosamente"
        except Exception as e:
            return False, f"Error al crear cliente: {str(e)}"
        
    #Modificada
    def crear_cliente(self, nombre, cedula):
        """Compatibilidad con la interfaz: recibe (nombre, cedula) y delega en registrar_cliente."""
        return self.registrar_cliente(cedula, nombre)
        

    def seleccionar_cliente(self, cedula):
        if cedula in self.cuentas:
            for cliente in self.clientes:
                if cliente.cedula == cedula:
                    self.cliente_actual = cliente
                    return True,  f"Cliente {cliente.nombre} seleccionado"
            return False, "Error al seleccionar el cliente"
        else:
            return False, "No existe el cliente con dicha cedula."
        
    #-----------------

    def obtener_lista_clientes(self):
        """Retorna lista de todos los clientes"""
        return self.clientes
    
    def obtener_cliente_actual(self):
        """Retorna el cliente actualmente seleccionado"""
        return self.cliente_actual
    
    def hay_cliente_seleccionado(self):
        """Verifica si hay un cliente seleccionado"""
        return self.cliente_actual is not None
    
    def obtener_cuenta_actual(self):
        """Retorna la cuenta del cliente seleccionado"""
        if self.cliente_actual:
            return self.cuentas.get(self.cliente_actual.cedula)
        return None
    
    def eliminar_cliente(self, cedula):
        """Elimina un cliente y su cuenta"""
        if cedula not in self.cuentas:
            return False, "Cliente no encontrado"
        
        # Buscar y eliminar de la lista
        cliente_a_eliminar = None
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                cliente_a_eliminar = cliente
                break
        
        if cliente_a_eliminar:
            self.clientes.remove(cliente_a_eliminar)
            del self.cuentas[cedula]
            
            # Si era el cliente actual, desseleccionar
            if self.cliente_actual and self.cliente_actual.cedula == cedula:
                self.cliente_actual = None
            
            return True, f"Cliente {cliente_a_eliminar.nombre} eliminado"
        
        return False, "Error al eliminar cliente"
    

     # ===== OPERACIONES CUENTA DE AHORRO =====
    
    def depositar_ahorro(self, monto):
        """Deposita dinero en la cuenta de ahorro del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado"
        
        try:
            monto = float(monto)
            if cuenta.cuenta_ahorro.depositar(monto):
                return True, f"Depósito exitoso: ${monto:,.2f}"
            else:
                return False, "El monto debe ser positivo"
        except ValueError:
            return False, "Monto inválido"
    
    def retirar_ahorro(self, monto):
        """Retira dinero de la cuenta de ahorro del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado"
        
        try:
            monto = float(monto)
            if cuenta.cuenta_ahorro.retirar(monto):
                return True, f"Retiro exitoso: ${monto:,.2f}"
            else:
                return False, "Fondos insuficientes o monto inválido"
        except ValueError:
            return False, "Monto inválido"
    
    # ===== OPERACIONES CUENTA CORRIENTE =====
    
    def depositar_corriente(self, monto):
        """Deposita dinero en la cuenta corriente del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado"
        
        try:
            monto = float(monto)
            if cuenta.cuenta_corriente.depositar(monto):
                return True, f"Depósito exitoso: ${monto:,.2f}"
            else:
                return False, "El monto debe ser positivo"
        except ValueError:
            return False, "Monto inválido"
    
    def retirar_corriente(self, monto):
        """Retira dinero de la cuenta corriente del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado"
        
        try:
            monto = float(monto)
            if cuenta.cuenta_corriente.retirar(monto):
                return True, f"Retiro exitoso: ${monto:,.2f}"
            else:
                return False, "Fondos insuficientes o monto inválido"
        except ValueError:
            return False, "Monto inválido"
    
    # ===== OPERACIONES CDT =====
    
    def abrir_cdt(self, monto, tasa_interes, desde_ahorro=True):
        """Abre un nuevo CDT para el cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado", None
        
        try:
            monto = float(monto)
            tasa_interes = float(tasa_interes) / 100  # Convertir porcentaje a decimal
            
            if monto <= 0 or tasa_interes <= 0:
                return False, "Monto y tasa deben ser positivos", None
            
            id_cdt = cuenta.abrir_cdt(monto, tasa_interes, desde_ahorro)
            
            if id_cdt:
                cuenta_origen = "ahorro" if desde_ahorro else "corriente"
                return True, f"CDT #{id_cdt} abierto exitosamente desde cuenta de {cuenta_origen}", id_cdt
            else:
                return False, "Fondos insuficientes en la cuenta origen", None
        except ValueError:
            return False, "Valores inválidos", None
    
    def cerrar_cdt(self, id_cdt):
        """Cierra un CDT específico del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado"
        
        try:
            id_cdt = int(id_cdt)
            monto_recuperado = cuenta.cerrar_cdt(id_cdt)
            
            if monto_recuperado is not None:
                return True, f"CDT #{id_cdt} cerrado. Monto transferido: ${monto_recuperado:,.2f}"
            else:
                return False, "CDT no encontrado"
        except ValueError:
            return False, "ID de CDT inválido"
    
    def obtener_cdts(self):
        """Retorna lista de CDTs activos del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return []
        
        return cuenta.get_todos_cdts()
    
    # ===== CONSULTAS =====
    
    def obtener_saldo_ahorro(self):
        """Retorna el saldo de la cuenta de ahorro del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return 0
        return cuenta.cuenta_ahorro.get_saldo()
    
    def obtener_saldo_corriente(self):
        """Retorna el saldo de la cuenta corriente del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return 0
        return cuenta.cuenta_corriente.get_saldo()
    
    def obtener_saldo_total(self):
        """Retorna el saldo total de todos los productos del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return 0
        return cuenta.get_saldo_total()
    
    def obtener_mes_actual(self):
        """Retorna el mes actual de la simulación del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return 0
        return cuenta.mes_actual
    
    def obtener_info_cliente(self):
        """Retorna información del cliente actual"""
        if not self.cliente_actual:
            return "Sin cliente seleccionado"
        return str(self.cliente_actual)
    
    # ===== SIMULACIÓN =====
    
    def avanzar_mes(self):
        """Avanza un mes en la simulación del cliente actual"""
        cuenta = self.obtener_cuenta_actual()
        if not cuenta:
            return False, "No hay cliente seleccionado", None
        
        resultado = cuenta.avanzar_mes()
        
        mensaje = f"Mes {resultado['mes']} completado\n"
        mensaje += f"Interés cuenta ahorro: ${resultado['interes_ahorro']:,.2f}\n"
        
        if resultado['intereses_cdts']:
            mensaje += "Intereses CDTs:\n"
            for id_cdt, interes in resultado['intereses_cdts'].items():
                mensaje += f"  CDT #{id_cdt}: ${interes:,.2f}\n"
        
        mensaje += f"Saldo total: ${resultado['saldo_total']:,.2f}"
        
        return True, mensaje, resultado
    
    def avanzar_mes_todos(self):
        """Avanza un mes para TODOS los clientes"""
        if not self.clientes:
            return False, "No hay clientes registrados"
        
        resultados = []
        for cliente in self.clientes:
            cuenta = self.cuentas[cliente.cedula]
            resultado = cuenta.avanzar_mes()
            resultados.append((cliente.nombre, resultado))
        
        mensaje = "Mes avanzado para todos los clientes:\n"
        for nombre, resultado in resultados:
            mensaje += f"\n{nombre}: Mes {resultado['mes']}, Saldo total: ${resultado['saldo_total']:,.2f}"
        
        return True, mensaje
        
