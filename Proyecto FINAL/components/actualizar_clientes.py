import tkinter as tk
from tkinter import messagebox

def mostrar_actualizacion_cliente(cliente_db):


    ventana = tk.Toplevel()
    ventana.geometry("640x480+500+300")  # Dimensiones y posición inicial
    ventana.resizable(False, False)  # Deshabilitar cambio de tamaño
    ventana.title("Actualizar Cliente")

    listbox = tk.Listbox(ventana)
    listbox.pack(fill=tk.BOTH, expand=True)

    clientes = cliente_db.ver_clientes()
    for cliente in clientes:
        listbox.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]}")

    def actualizar_cliente():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Cliente", "Debe seleccionar un cliente para actualizar.")
            return
        cliente_id = clientes[seleccion[0]][0]

        # Obtener los datos actuales del cliente
        cliente_actual = cliente_db.ver_cliente(cliente_id)[0]

        # Crear ventana para editar los datos del producto seleccionado
        actualizacion_ventana = tk.Toplevel()
        actualizacion_ventana.title("Editar datos del Cliente")
        actualizacion_ventana.geometry("500x400")  # Dimensiones
        actualizacion_ventana.resizable(False, False)  # Deshabilitar cambio de tamaño

        # Configurar las columnas de la cuadrícula para ajustar el ancho
        actualizacion_ventana.grid_columnconfigure(0, weight=1)  # Columna de etiquetas
        actualizacion_ventana.grid_columnconfigure(1, weight=3)  # Columna de entradas

        tk.Label(actualizacion_ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        nombre_entry = tk.Entry(actualizacion_ventana)
        nombre_entry.insert(0, cliente_actual[1])  # Nombre actual
        nombre_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        apellido_entry = tk.Entry(actualizacion_ventana)
        apellido_entry.insert(0, cliente_actual[2])  # Apellido actual
        apellido_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_ventana, text="Teléfono:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        telefono_entry = tk.Entry(actualizacion_ventana)
        telefono_entry.insert(0, cliente_actual[3])  # Teléfono actual
        telefono_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_ventana, text="Email:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        email_entry = tk.Entry(actualizacion_ventana)
        email_entry.insert(0, cliente_actual[4])  # Email actual
        email_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_ventana, text="Dirección:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
        direccion_entry = tk.Entry(actualizacion_ventana)
        direccion_entry.insert(0, cliente_actual[5])  # Dirección actual
        direccion_entry.grid(row=4, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")


        def validar_datos():
            nombre = nombre_entry.get().strip()
            apellido = apellido_entry.get().strip()
            telefono = telefono_entry.get().strip()
            email = email_entry.get().strip()
            direccion = direccion_entry.get().strip()

            # Validar que los campos no estén vacíos y sean correctos
            if not nombre:
                messagebox.showerror("Error de Validación", "El nombre no puede estar vacío.")
                return False
            if not apellido:
                messagebox.showerror("Error de Validación", "El apellido no puede estar vacío.")
                return False
            if not telefono.replace('.', '', 1).isdigit():
                messagebox.showerror("Error de Validación", "El telefono debe ser un número válido.")
                return False
            if not email:
                messagebox.showerror("Error de Validación", "El correo electronico no puede estar vacio.")
                return False
            if not direccion:
                messagebox.showerror("Error de Validación", "La direccion no puede estar vacía.")
                return False

            return True

        def guardar_cambios():

            if validar_datos():
                nombre = nombre_entry.get()
                apellido = apellido_entry.get()
                telefono = telefono_entry.get()
                email = email_entry.get()
                direccion = direccion_entry.get()
                
                cliente_db.actualizar_cliente(cliente_id, nombre, apellido, telefono, email, direccion)
                messagebox.showinfo("Éxito", "Cliente actualizado con éxito.")
                actualizacion_ventana.destroy()

        tk.Button(actualizacion_ventana, text="Guardar Cambios", command=guardar_cambios, bd=1).grid(row=5, column=0, columnspan=2, pady=20)

    tk.Button(ventana, text="Actualizar Cliente Seleccionado", command=actualizar_cliente, bd=1).pack(pady=10)
