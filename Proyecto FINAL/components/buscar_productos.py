import tkinter as tk
from tkinter import messagebox, ttk

# Función principal para buscar productos en la base de datos
def buscar_productos(producto_db):
    # Crear una ventana secundaria (Toplevel)
    window = tk.Toplevel()
    window.geometry("400x220+500+300")  # Configura el tamaño y posición de la ventana
    window.resizable(False, False)  # Evita que la ventana sea redimensionada
    window.title("Buscar producto")  # Título de la ventana

    # Configuración de la grilla de la ventana principal
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=3)

    # Etiqueta principal para instrucciones
    tk.Label(window, text="Ingrese el nombre del producto que desea buscar").grid(
        row=0, column=0, columnspan=2, pady=20
    )

    # Etiqueta y campo de entrada para el nombre del producto
    tk.Label(window, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    nombre_entry = tk.Entry(window)  # Entrada para escribir el nombre
    nombre_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

    # Función para abrir la ventana con la lista de productos encontrados
    def abrir_lista_productos(vendidos=False):

        if not nombre_entry.get():
            messagebox.showwarning("Buscar Productos", "Por favor, ingrese algo.")
            return



        nombre_producto = nombre_entry.get().strip()  # Obtiene el valor del campo de entrada
        window.destroy()  # Cierra la ventana principal

        # Crear una nueva ventana para mostrar los productos encontrados
        list_window = tk.Toplevel()
        list_window.title("Productos encontrados")
        list_window.geometry("640x480")  # Tamaño de la ventana
        list_window.resizable(False, False)  # No redimensionable

        # Configuración de la grilla de la nueva ventana
        list_window.grid_columnconfigure(0, weight=1)
        list_window.grid_columnconfigure(1, weight=1)

        # Listbox para mostrar los productos
        listbox = tk.Listbox(list_window)
        listbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        # Buscar productos en la base de datos usando el nombre ingresado
        productos = producto_db.buscar_producto_por_nombre(nombre_producto, vendidos)
        for producto in productos:
            listbox.insert(tk.END, f"ID: {producto[0]}   |    Nombre: {producto[1]}   |   Precio: ${producto[3]}   |   Stock: {producto[4]}  |  Vendidos: {producto[5]}")




        # Función para editar un producto seleccionado
        def editar_producto():
            seleccion = listbox.curselection()  # Obtiene el índice del producto seleccionado
            if not seleccion:
                messagebox.showwarning("Error", "Seleccione un producto para editar.")
                return

            producto_id = productos[seleccion[0]][0]  # Obtiene el ID del producto
            producto_actual = producto_db.ver_producto(producto_id)[0]  # Recupera los datos del producto

            # Crear una ventana para editar el producto
            edit_window = tk.Toplevel()
            edit_window.title("Editar Producto")
            edit_window.geometry("400x300")
            edit_window.resizable(False, False)

            # Configuración de la grilla
            for i in range(2):
                edit_window.grid_columnconfigure(i, weight=1)

            # Crear etiquetas y campos de entrada para los datos del producto
            fields = ["Nombre", "Descripción", "Precio", "Stock"]
            entries = {}  # Diccionario para almacenar las entradas
            for idx, field in enumerate(fields):
                tk.Label(edit_window, text=f"{field}:").grid(row=idx, column=0, padx=10, pady=5, sticky="e")
                entry = tk.Entry(edit_window)
                entry.grid(row=idx, column=1, padx=10, pady=5, ipadx=10, sticky="ew")
                entry.insert(0, str(producto_actual[idx + 1]))  # Precarga los valores actuales
                entries[field.lower()] = entry

            # Función para guardar los cambios del producto
            def guardar_cambios():
                try:
                    # Recopila los datos del formulario y los valida
                    datos = {
                        "nombre": entries["nombre"].get().strip(),
                        "descripcion": entries["descripción"].get().strip(),
                        "precio": float(entries["precio"].get()),
                        "stock": int(entries["stock"].get()),
                    }
                except ValueError:
                    messagebox.showerror("Error", "Datos inválidos. Revise los campos.")
                    return

                # Actualiza el producto en la base de datos
                producto_db.actualizar_producto(producto_id, **datos)
                messagebox.showinfo("Éxito", "Producto actualizado con éxito.")
                edit_window.destroy()  # Cierra la ventana de edición

            # Botón para guardar los cambios
            tk.Button(edit_window, text="Guardar Cambios", command=guardar_cambios).grid(
                row=len(fields), column=0, columnspan=2, pady=10
            )

        # Función para eliminar un producto seleccionado
        def eliminar_producto():
            seleccion = listbox.curselection()  # Obtiene el índice del producto seleccionado
            if not seleccion:
                messagebox.showwarning("Error", "Seleccione un producto para eliminar.")
                return

            producto_id = productos[seleccion[0]][0]  # Obtiene el ID del producto
            confirmacion = messagebox.askyesno(
                "Confirmar Eliminación", f"¿Desea eliminar el producto con ID {producto_id}?"
            )
            if confirmacion:
                producto_db.eliminar_producto(producto_id)  # Elimina el producto de la base de datos
                listbox.delete(seleccion)  # Lo elimina también del Listbox
                messagebox.showinfo("Éxito", "Producto eliminado con éxito.")

        # Botones de acción en la ventana de lista
        tk.Button(list_window, text="Editar producto", command=editar_producto, bd=1).grid(row=1, column=0, pady=10, padx=5, sticky="e")
        tk.Button(list_window, text="Eliminar producto", command=eliminar_producto, bd=1).grid(row=1, column=1, pady=10, padx=5, sticky="w")



    # Botón para iniciar la búsqueda de productos
    tk.Button(window, text="Buscar Producto", command=lambda:abrir_lista_productos(False), bd=1).grid(row=2, column=0, columnspan=2, pady=10)

    # Boton para iniciar la busqueda filtrada de productos -> por Ventas
    tk.Button(window, text="Filtrar por Mas Vendidos", command= lambda: abrir_lista_productos(True), bd=1).grid(row=3, column=0, columnspan=2, pady=10)
 
