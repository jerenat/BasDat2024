import tkinter as tk


def ver_productos(producto_db):

    # Crear ventana principal para la vista de productos
    window = tk.Toplevel()
    window.geometry("640x480+500+300")  # Dimensiones y posición inicial
    window.resizable(False, False)  # Deshabilitar cambio de tamaño
    window.title("Ver todos los productos")  # Título de la ventana
    
    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    for producto in producto_db.ver_productos():
        listbox.insert(tk.END, f"ID: {producto[0]}   |    Nombre: {producto[1]}   |   Precio: ${producto[3]}   |   Stock: {producto[4]}  |  Vendidos: {producto[5]}")
