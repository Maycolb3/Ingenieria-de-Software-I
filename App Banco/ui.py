import tkinter as tk
from tkinter import ttk, messagebox
from banco import Banco

class BancoView:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancario - Simulación")
        self.root.geometry("800x600")
        
        self.controller = Banco()
        
        self.crear_interfaz()
        
    def crear_interfaz(self):

        frame_clientes = ttk.LabelFrame(self.root, text="Gestión de Clientes", padding=10)
        frame_clientes.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_clientes, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5)
        self.entry_nombre = ttk.Entry(frame_clientes, width=20)
        self.entry_nombre.grid(row=0, column=1, padx=5)
        
        ttk.Label(frame_clientes, text="Cédula:").grid(row=0, column=2, sticky="w", padx=5)
        self.entry_cedula = ttk.Entry(frame_clientes, width=15)
        self.entry_cedula.grid(row=0, column=3, padx=5)
        
        ttk.Button(frame_clientes, text="Crear Cliente", 
                   command=self.crear_cliente).grid(row=0, column=4, padx=5)
        
        ttk.Label(frame_clientes, text="Cliente actual:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.combo_clientes = ttk.Combobox(frame_clientes, state="readonly", width=30)
        self.combo_clientes.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.combo_clientes.bind("<<ComboboxSelected>>", self.seleccionar_cliente)
        
        self.label_info_cliente = ttk.Label(frame_clientes, text="Sin cliente seleccionado", 
                                            font=("Arial", 10, "bold"))
        self.label_info_cliente.grid(row=1, column=3, columnspan=2, padx=5, pady=5)
        
        frame_operaciones = ttk.LabelFrame(self.root, text="Operaciones Bancarias", padding=10)
        frame_operaciones.pack(fill="both", expand=True, padx=10, pady=5)
        
        frame_ahorro = ttk.LabelFrame(frame_operaciones, text="Cuenta de Ahorro", padding=10)
        frame_ahorro.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(frame_ahorro, text="Monto:").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_monto_ahorro = ttk.Entry(frame_ahorro, width=15)
        self.entry_monto_ahorro.grid(row=0, column=1, pady=2)
        
        ttk.Button(frame_ahorro, text="Depositar", 
                   command=self.depositar_ahorro).grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        ttk.Button(frame_ahorro, text="Retirar", 
                   command=self.retirar_ahorro).grid(row=2, column=0, columnspan=2, pady=2, sticky="ew")
        
        self.label_saldo_ahorro = ttk.Label(frame_ahorro, text="Saldo: $0.00", 
                                            font=("Arial", 10, "bold"))
        self.label_saldo_ahorro.grid(row=3, column=0, columnspan=2, pady=10)
        
        frame_corriente = ttk.LabelFrame(frame_operaciones, text="Cuenta Corriente", padding=10)
        frame_corriente.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(frame_corriente, text="Monto:").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_monto_corriente = ttk.Entry(frame_corriente, width=15)
        self.entry_monto_corriente.grid(row=0, column=1, pady=2)
        
        ttk.Button(frame_corriente, text="Depositar", 
                   command=self.depositar_corriente).grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")
        ttk.Button(frame_corriente, text="Retirar", 
                   command=self.retirar_corriente).grid(row=2, column=0, columnspan=2, pady=2, sticky="ew")
        
        self.label_saldo_corriente = ttk.Label(frame_corriente, text="Saldo: $0.00", 
                                               font=("Arial", 10, "bold"))
        self.label_saldo_corriente.grid(row=3, column=0, columnspan=2, pady=10)
        
        frame_cdt = ttk.LabelFrame(frame_operaciones, text="Certificados de Depósito (CDT)", padding=10)
        frame_cdt.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(frame_cdt, text="Monto:").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_monto_cdt = ttk.Entry(frame_cdt, width=15)
        self.entry_monto_cdt.grid(row=0, column=1, pady=2)
        
        ttk.Label(frame_cdt, text="Tasa (%):").grid(row=1, column=0, sticky="w", pady=2)
        self.entry_tasa_cdt = ttk.Entry(frame_cdt, width=15)
        self.entry_tasa_cdt.grid(row=1, column=1, pady=2)
        
        ttk.Label(frame_cdt, text="Desde:").grid(row=2, column=0, sticky="w", pady=2)
        self.combo_origen_cdt = ttk.Combobox(frame_cdt, values=["Ahorro", "Corriente"], 
                                             state="readonly", width=12)
        self.combo_origen_cdt.grid(row=2, column=1, pady=2)
        self.combo_origen_cdt.current(0)
        
        ttk.Button(frame_cdt, text="Abrir CDT", 
                   command=self.abrir_cdt).grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")
        
        ttk.Label(frame_cdt, text="CDTs activos:").grid(row=4, column=0, columnspan=2, sticky="w", pady=(10,2))
        self.listbox_cdts = tk.Listbox(frame_cdt, height=4, width=25)
        self.listbox_cdts.grid(row=5, column=0, columnspan=2, pady=2)
        
        ttk.Button(frame_cdt, text="Cerrar CDT", 
                   command=self.cerrar_cdt).grid(row=6, column=0, columnspan=2, pady=2, sticky="ew")
        
        frame_operaciones.columnconfigure(0, weight=1)
        frame_operaciones.columnconfigure(1, weight=1)
        frame_operaciones.columnconfigure(2, weight=1)
        
        frame_resumen = ttk.LabelFrame(self.root, text="Resumen y Simulación", padding=10)
        frame_resumen.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_resumen, text="Saldo Total:").grid(row=0, column=0, sticky="w", padx=5)
        self.label_saldo_total = ttk.Label(frame_resumen, text="$0.00", 
                                          font=("Arial", 14, "bold"), foreground="green")
        self.label_saldo_total.grid(row=0, column=1, sticky="w", padx=5)
        
        ttk.Label(frame_resumen, text="Mes actual:").grid(row=0, column=2, sticky="w", padx=20)
        self.label_mes = ttk.Label(frame_resumen, text="0", 
                                   font=("Arial", 14, "bold"), foreground="blue")
        self.label_mes.grid(row=0, column=3, sticky="w", padx=5)
        
        ttk.Button(frame_resumen, text="⏭ Avanzar Mes", 
                   command=self.avanzar_mes, 
                   style="Accent.TButton").grid(row=0, column=4, padx=20)
        
        ttk.Label(frame_resumen, text="Historial:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        
        self.text_historial = tk.Text(frame_resumen, height=6, width=80, state="disabled")
        self.text_historial.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
        
        scrollbar = ttk.Scrollbar(frame_resumen, command=self.text_historial.yview)
        scrollbar.grid(row=2, column=5, sticky="ns", pady=5)
        self.text_historial.config(yscrollcommand=scrollbar.set)
    
    def crear_cliente(self):
        nombre = self.entry_nombre.get().strip()
        cedula = self.entry_cedula.get().strip()
        
        exito, mensaje = self.controller.crear_cliente(nombre, cedula)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_combo_clientes()
            self.actualizar_vista()
            # Limpiar campos
            self.entry_nombre.delete(0, tk.END)
            self.entry_cedula.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)
    
    def seleccionar_cliente(self, event=None):
        seleccion = self.combo_clientes.get()
        if seleccion:
            cedula = seleccion.split("CC: ")[1].rstrip(")")
            exito, mensaje = self.controller.seleccionar_cliente(cedula)
            
            if exito:
                self.agregar_mensaje(mensaje)
                self.actualizar_vista()
            else:
                messagebox.showerror("Error", mensaje)
    
    def depositar_ahorro(self):
        monto = self.entry_monto_ahorro.get()
        exito, mensaje = self.controller.depositar_ahorro(monto)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
            self.entry_monto_ahorro.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)

    
    def retirar_ahorro(self):
        monto = self.entry_monto_ahorro.get()
        exito, mensaje = self.controller.retirar_ahorro(monto)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
            self.entry_monto_ahorro.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)
    
    def depositar_corriente(self):
        monto = self.entry_monto_corriente.get()
        exito, mensaje = self.controller.depositar_corriente(monto)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
            self.entry_monto_corriente.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)
    
    def retirar_corriente(self):
        monto = self.entry_monto_corriente.get()
        exito, mensaje = self.controller.retirar_corriente(monto)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
            self.entry_monto_corriente.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)
    
    def abrir_cdt(self):
        monto = self.entry_monto_cdt.get()
        tasa = self.entry_tasa_cdt.get()
        desde_ahorro = self.combo_origen_cdt.get() == "Ahorro"
        
        exito, mensaje, id_cdt = self.controller.abrir_cdt(monto, tasa, desde_ahorro)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
            self.entry_monto_cdt.delete(0, tk.END)
            self.entry_tasa_cdt.delete(0, tk.END)
        else:
            messagebox.showerror("Error", mensaje)
    
    def cerrar_cdt(self):
        seleccion = self.listbox_cdts.curselection()
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un CDT para cerrar")
            return
        
        texto = self.listbox_cdts.get(seleccion[0])
        id_cdt = int(texto.split("#")[1].split(":")[0])
        
        exito, mensaje = self.controller.cerrar_cdt(id_cdt)
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
        else:
            messagebox.showerror("Error", mensaje)
    
    def avanzar_mes(self):
        exito, mensaje, resultado = self.controller.avanzar_mes()
        
        if exito:
            self.agregar_mensaje(mensaje)
            self.actualizar_vista()
        else:
            messagebox.showerror("Error", mensaje)
    
    def actualizar_combo_clientes(self):
        clientes = self.controller.obtener_lista_clientes()
        valores = [f"{cliente.nombre} (CC: {cliente.cedula})" for cliente in clientes]
        self.combo_clientes['values'] = valores
        
        if valores:
            self.combo_clientes.current(len(valores) - 1)
    
    def actualizar_vista(self):
        if not self.controller.hay_cliente_seleccionado():
            return
            
        cliente = self.controller.obtener_cliente_actual()
        self.label_info_cliente.config(text=f"{cliente.nombre} (CC: {cliente.cedula})")
        
        saldo_ahorro = self.controller.obtener_saldo_ahorro()
        saldo_corriente = self.controller.obtener_saldo_corriente()
        saldo_total = self.controller.obtener_saldo_total()
        
        self.label_saldo_ahorro.config(text=f"Saldo: ${saldo_ahorro:,.2f}")
        self.label_saldo_corriente.config(text=f"Saldo: ${saldo_corriente:,.2f}")
        self.label_saldo_total.config(text=f"${saldo_total:,.2f}")
        
        mes = self.controller.obtener_mes_actual()
        self.label_mes.config(text=str(mes))
        
        self.listbox_cdts.delete(0, tk.END)
        cdts = self.controller.obtener_cdts()
        for cdt in cdts:
            texto = f"CDT #{cdt._Cdt__id}: ${cdt.saldo:,.2f} ({cdt._Cdt__interes_mensual*100:.2f}%)"
            self.listbox_cdts.insert(tk.END, texto)
    
    def agregar_mensaje(self, mensaje):
        self.text_historial.config(state="normal")
        self.text_historial.insert(tk.END, f"• {mensaje}\n")
        self.text_historial.see(tk.END)  
        self.text_historial.config(state="disabled")
