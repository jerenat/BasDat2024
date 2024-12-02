import tkinter as tk
from tkinter import messagebox


def mostrar_clientes(cliente_db):
    ventana = tk.Toplevel()
    ventana.geometry("640x480+500+300")  # Dimensiones y posición inicial
    ventana.resizable(False, False)  # Deshabilitar cambio de tamaño
    ventana.title("Ver Clientes")
    
    listbox = tk.Listbox(ventana)
    listbox.pack(fill=tk.BOTH, expand=True)

    for cliente in cliente_db.ver_clientes():
        listbox.insert(tk.END, f"ID: {cliente[0]}   |   Nombre y Apellido: {cliente[1]} {cliente[2]}   |   Telefono: {cliente[3]}")
