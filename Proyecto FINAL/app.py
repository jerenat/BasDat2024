import tkinter as tk
from context.clientes import Cliente
from context.ordenes import Ordenes
from context.productos import Producto
from models.conexion import BaseDeDatos


# -- Importar las GUIs
from gui_client import mostrar_gestion_clientes
from gui_ventas import mostrar_gestion_productos
from gui_acerca import mostrar_acerca_de
from gui_ordenes import mostrar_gestion_ordenes


# Conectar a la base de datos
db = BaseDeDatos("localhost", "root", "", "basededatosi")
db.conectar()
cliente_db = Cliente(db)
ordenes_db = Ordenes(db)
producto_db = Producto(db)

# Ventana principal
root = tk.Tk()

root.geometry("720x400")

root.resizable(False, False)

root.title("Sistema de Ventas - v0.0.1")

# Configurar las columnas para que se distribuyan equitativamente
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


tk.Label(root,text="Bienvenido/a",font=("Arial", 17),justify="center").grid(row=0, column=0, sticky="nsew", pady=10)


# -- BOTONES

# -- AREA CLIENTES
cliente_img = tk.PhotoImage(file="images/cliente.png")
reg_cliente = tk.Button(root, text="Area Clientes", image=cliente_img, compound="top", padx=20, pady=10, bd=1, command=lambda: mostrar_gestion_clientes(cliente_db, ordenes_db))
reg_cliente.grid(row=2, column=0, sticky="nsew", padx=15, pady=5)

# -- AREA PRODUCTOS
producto_img = tk.PhotoImage(file="images/productos.png")
reg_producto = tk.Button(root, text="Area Productos", image=producto_img, compound="top", padx=20, pady=10, bd=1, command=lambda: mostrar_gestion_productos(producto_db))
reg_producto.grid(row=2, column=1, sticky="nsew", padx=15, pady=5)

# -- AREA ORDENES
ordenes_img = tk.PhotoImage(file="images/ordenes.png")
reg_ordenes = tk.Button(root, text="Area Ordenes", image=ordenes_img, compound="top", padx=20, pady=10, bd=1, command = lambda: mostrar_gestion_ordenes(cliente_db, producto_db, ordenes_db))
reg_ordenes.grid(row=2, column=2, sticky="nsew", padx=15, pady=5)

# -- AREA ACERCA DE
acerca_img = tk.PhotoImage(file="images/info.png")
reg_acerca = tk.Button(root, text="Acerca de", image=acerca_img, compound="top", padx=20, pady=10, bd=1, command=lambda: mostrar_acerca_de())
reg_acerca.grid(row=2, column=3, sticky="nsew", padx=15, pady=5)

root.mainloop()

# Cerrar conexión al final
db.desconectar()
