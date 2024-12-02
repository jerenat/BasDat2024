import tkinter as tk
from components.registrar_clientes import mostrar_registro_cliente
from components.actualizar_clientes import mostrar_actualizacion_cliente
from components.eliminar_clientes import mostrar_eliminacion_cliente
from components.ver_clientes import mostrar_clientes
from components.buscar_clientes import buscar_clientes

def mostrar_gestion_clientes(cliente_db, ordenes_db):
    """
    Función para mostrar la ventana principal de gestión de clientes.
    """
    # Ventana principal
    root = tk.Tk()
    root.geometry("720x300")
    root.resizable(False, False)
    root.title("Gestión de Clientes")

    # Configurar las columnas del grid para que se expandan
    root.grid_columnconfigure(0, weight=1)

    # Botones con sus respectivas funciones
    tk.Button(root, text="Ver Clientes", padx=20, pady=10, bd=1,
              command=lambda: mostrar_clientes(cliente_db)).grid(row=0, column=0, sticky="ew", padx=15, pady=5)
    
    tk.Button(root, text="Buscar clientes por Nombre", padx=20, pady=10, bd=1,
              command=lambda: buscar_clientes(cliente_db)).grid(row=1, column=0, sticky="ew", padx=15, pady=5)
    
    tk.Button(root, text="Nuevo Cliente", padx=20, pady=10, bd=1,
              command=lambda: mostrar_registro_cliente(cliente_db)).grid(row=2, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Actualizar Cliente", padx=20, pady=10, bd=1,
              command=lambda: mostrar_actualizacion_cliente(cliente_db)).grid(row=3, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Eliminar Cliente", padx=20, pady=10, bd=1,
              command=lambda: mostrar_eliminacion_cliente(cliente_db)).grid(row=4, column=0, sticky="ew", padx=15, pady=5)
    

    # Ejecutar la ventana principal
    root.mainloop()
