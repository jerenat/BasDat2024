import tkinter as tk
from components.registrar_productos import registrar_productos
from components.actualizar_productos import actualizar_productos
from components.eliminar_productos import eliminar_productos
from components.ver_productos import ver_productos
from components.buscar_productos import buscar_productos

def mostrar_gestion_productos(producto_db):
    """
    Función para mostrar la ventana principal de gestión de productos.
    """
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Gestión de Productos")
    root.geometry("720x280")
    root.resizable(False, False)

    # Configurar las columnas del grid para que se expandan
    root.grid_columnconfigure(0, weight=1)

    # Botones con sus respectivas funciones
    tk.Button(root, text="Registrar Productos", padx=20, pady=10, bd=1,
              command=lambda: registrar_productos(producto_db)).grid(row=0, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Actualizar Producto", padx=20, pady=10, bd=1,
              command=lambda: actualizar_productos(producto_db)).grid(row=1, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Eliminar Producto", padx=20, pady=10, bd=1,
              command=lambda: eliminar_productos(producto_db)).grid(row=2, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Ver Productos", padx=20, pady=10, bd=1,
              command=lambda: ver_productos(producto_db)).grid(row=3, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Buscar Producto", padx=20, pady=10, bd=1,
              command=lambda: buscar_productos(producto_db)).grid(row=4, column=0, sticky="ew", padx=15, pady=5)

    # Ejecutar la ventana principal
    root.mainloop()
