import tkinter as tk
from tkinter import messagebox

def mostrar_registro_cliente(cliente_db):
    ventana = tk.Toplevel()
    ventana.geometry("700x300+500+500")
    ventana.resizable(False, False)
    ventana.title("Nuevo cliente")
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 se ajuste dinámicamente
    ventana.grid_columnconfigure(1, weight=3)  # Hacer que la columna 1 sea más amplia

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=10)
    nombre_entry = tk.Entry(ventana)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=5, pady=10)
    apellido_entry = tk.Entry(ventana)
    apellido_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(ventana, text="Teléfono:").grid(row=2, column=0, padx=5, pady=10)
    telefono_entry = tk.Entry(ventana)
    telefono_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=10)
    email_entry = tk.Entry(ventana)
    email_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    tk.Label(ventana, text="Dirección:").grid(row=4, column=0, padx=5, pady=10)
    direccion_entry = tk.Entry(ventana)
    direccion_entry.grid(row=4, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    def registrar_cliente():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        telefono = telefono_entry.get()
        email = email_entry.get()
        direccion = direccion_entry.get()


        # Validaciones
        if not nombre:
            messagebox.showerror("Error", "El campo 'Nombre' es obligatorio.")
            return
        if not apellido:
            messagebox.showerror("Error", "El campo 'Apellido' es obligatorio.")
            return
        
        if not telefono.replace('.', '', 1).isdigit():    
            messagebox.showerror("Error", "El 'Telefono' es obligatorio y debe ser un número válido.")
            return
        if not email:
            messagebox.showerror("Error", "El campo 'Email' es obligatorio.")
            return
        if not direccion:
            messagebox.showerror("Error", "El campo 'Dirección' es obligatorio.")
            return



        cliente_db.registrar_cliente(nombre, apellido, telefono, email, direccion)
        messagebox.showinfo("Éxito", "Cliente registrado con éxito.")
        ventana.destroy()

    tk.Button(ventana, text="Registrar Cliente ahora", command=registrar_cliente, bd=1).grid(row=5, columnspan=2, pady=20)
