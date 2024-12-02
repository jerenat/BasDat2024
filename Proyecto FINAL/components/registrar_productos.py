import tkinter as tk
from tkinter import messagebox

def registrar_productos(producto_db):
    window = tk.Toplevel()
    window.geometry("700x300+500+500")
    window.resizable(False, False)
    window.title("Agregar producto(s)")
    window.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 se ajuste dinámicamente
    window.grid_columnconfigure(1, weight=3)  # Hacer que la columna 1 sea más amplia

    # Campos del formulario
    tk.Label(window, text="Nombre:").grid(row=0, column=0, padx=5, pady=10)
    nombre_entry = tk.Entry(window)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(window, text="Descripcion:").grid(row=1, column=0, padx=5, pady=10)
    descripcion_entry = tk.Entry(window)
    descripcion_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(window, text="Precio:").grid(row=2, column=0, padx=5, pady=10)
    precio_entry = tk.Entry(window)
    precio_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(window, text="Stock?:").grid(row=3, column=0, padx=5, pady=10)
    stock_entry = tk.Entry(window)
    stock_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    # Validación y registro
    def registrar_producto():
        nombre = nombre_entry.get().strip()
        descripcion = descripcion_entry.get().strip()
        precio = precio_entry.get().strip()
        stock = stock_entry.get().strip()

        # Validaciones
        if not nombre:
            messagebox.showerror("Error", "El campo 'Nombre' es obligatorio.")
            return
        if not descripcion:
            messagebox.showerror("Error", "El campo 'Descripcion' es obligatorio.")
            return
        try:
            precio = float(precio)
            if precio <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El campo 'Precio' debe ser un número positivo.")
            return
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El campo 'Stock' debe ser un número entero no negativo.")
            return

        # Registro del producto en la base de datos
        producto_db.registrar_producto(nombre, descripcion, precio, stock)
        messagebox.showinfo("Información", "El producto ha sido registrado con éxito.")
        window.destroy()

    # Botón para registrar
    btn_RegistrarProducto = tk.Button(window, text="Registrar Producto ahora", command=registrar_producto, bd=1)
    btn_RegistrarProducto.grid(row=5, column=0, columnspan=2, pady=20)

