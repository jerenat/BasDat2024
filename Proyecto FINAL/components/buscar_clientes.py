import tkinter as tk
from tkinter import messagebox, ttk

# Función principal para buscar clientes en la base de datos
def buscar_clientes(cliente_db):
    # Crear una ventana secundaria (Toplevel)
    window = tk.Toplevel()
    window.geometry("400x170+500+300")  # Configura el tamaño y posición de la ventana
    window.resizable(False, False)  # Evita que la ventana sea redimensionada
    window.title("Buscar Cliente(s)")  # Título de la ventana

    # Configuración de la grilla de la ventana principal
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=3)

    # Etiqueta principal para instrucciones
    tk.Label(window, text="Ingrese el nombre del cliente que desea buscar").grid(
        row=0, column=0, columnspan=2, pady=20
    )

    # Etiqueta y campo de entrada para el nombre del cliente
    tk.Label(window, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    nombre_entry = tk.Entry(window)  # Entrada para escribir el nombre
    nombre_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    # Función para abrir la ventana con la lista de clientes encontrados
    def abrir_lista_clientes():
        nombre_cliente = nombre_entry.get().strip()  # Obtiene el valor del campo de entrada
        window.destroy()  # Cierra la ventana principal

        # Crear una nueva ventana para mostrar los clientes encontrados
        list_window = tk.Toplevel()
        list_window.title("Cliente(s) encontrado(s)")
        list_window.geometry("640x480")  # Tamaño de la ventana
        list_window.resizable(False, False)  # No redimensionable

        # Configuración de la grilla de la nueva ventana
        list_window.grid_columnconfigure(0, weight=1)
        list_window.grid_columnconfigure(1, weight=1)

        # Listbox para mostrar los clientes
        listbox = tk.Listbox(list_window)
        listbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Buscar clientes en la base de datos usando el nombre ingresado
        clientes = cliente_db.buscar_cliente_por_nombre(nombre_cliente)  # Recupera los clientes coincidentes
        for cliente in clientes:
            listbox.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]}")  # Muestra ID, nombre y apellido

        # Función para editar un cliente seleccionado
        def editar_cliente():
            seleccion = listbox.curselection()  # Obtiene el índice del cliente seleccionado
            if not seleccion:
                # Muestra una advertencia si no se selecciona ningún cliente
                messagebox.showwarning("Error", "Seleccione un cliente para editar.")
                return

            cliente_id = clientes[seleccion[0]][0]  # Obtiene el ID del cliente seleccionado
            cliente_actual = cliente_db.ver_cliente(cliente_id)[0]  # Recupera los datos del cliente

            # Crear una ventana para editar el cliente
            edit_window = tk.Toplevel()
            edit_window.title("Editar Cliente")
            edit_window.geometry("400x300")  # Tamaño de la ventana
            edit_window.resizable(False, False)  # No redimensionable

            # Configuración de la grilla
            for i in range(2):
                edit_window.grid_columnconfigure(i, weight=1)

            # Crear etiquetas y campos de entrada para los datos del cliente
            fields = ["Nombre", "Apellido", "Telefono", "Direccion", "Email"]
            entries = {}  # Diccionario para almacenar las entradas
            for idx, field in enumerate(fields):
                tk.Label(edit_window, text=f"{field}:").grid(row=idx, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(edit_window)
                entry.grid(row=idx, column=1, padx=10, pady=5, ipadx=10, sticky="ew")
                entry.insert(0, str(cliente_actual[idx + 1]))  # Precarga los valores actuales
                entries[field.lower()] = entry

            # Función para guardar los cambios del cliente
            def guardar_cambios():
                try:
                    # Recopila los datos del formulario y los valida
                    datos = {
                        "nombre": entries["nombre"].get().strip(),
                        "apellido": entries["apellido"].get().strip(),
                        "telefono": int(entries["telefono"].get()),
                        "direccion": entries["direccion"].get(),
                        "email": entries["email"].get().strip()
                    }
                except ValueError:
                    # Muestra un error si los datos no son válidos
                    messagebox.showerror("Error", "Datos inválidos. Revise los campos.")
                    return

                # Actualiza el cliente en la base de datos
                cliente_db.actualizar_cliente(cliente_id, **datos)
                messagebox.showinfo("Éxito", "Cliente actualizado con éxito.")
                edit_window.destroy()  # Cierra la ventana de edición

            # Botón para guardar los cambios
            tk.Button(edit_window, text="Guardar Cambios", command=guardar_cambios).grid(
                row=len(fields), column=0, columnspan=2, pady=10
            )

        # Función para eliminar un cliente seleccionado
        def eliminar_cliente():
            seleccion = listbox.curselection()  # Obtiene el índice del cliente seleccionado
            if not seleccion:
                # Muestra una advertencia si no se selecciona ningún cliente
                messagebox.showwarning("Error", "Seleccione un cliente para eliminar.")
                return

            cliente_id = clientes[seleccion[0]][0]  # Obtiene el ID del cliente seleccionado
            # Confirma antes de eliminar el cliente
            confirmacion = messagebox.askyesno(
                "Confirmar Eliminación", f"¿Desea eliminar el cliente con ID {cliente_id}?"
            )
            if confirmacion:
                cliente_db.eliminar_cliente(cliente_id)  # Elimina el cliente de la base de datos
                listbox.delete(seleccion)  # Lo elimina también del Listbox
                messagebox.showinfo("Éxito", "Cliente eliminado con éxito.")

        # Botones de acción en la ventana de lista
        tk.Button(list_window, text="Editar Cliente", command=editar_cliente, bd=1).grid(row=1, column=0, pady=10, padx=5, sticky="e")
        tk.Button(list_window, text="Eliminar Cliente", command=eliminar_cliente, bd=1).grid(row=1, column=1, pady=10, padx=5, sticky="w")

    # Botón para iniciar la búsqueda de clientes
    tk.Button(window, text="Buscar Cliente", command=abrir_lista_clientes, bd=1).grid(row=2, column=0, columnspan=2, pady=10)
