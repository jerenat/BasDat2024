import tkinter as tk
from tkinter import messagebox, ttk

def actualizar_productos(producto_db):

    # Crear ventana principal para la actualización de productos
    window = tk.Toplevel()
    window.geometry("640x480+500+300")  # Dimensiones y posición inicial
    window.resizable(False, False)  # Deshabilitar cambio de tamaño
    window.title("Actualizar productos")  # Título de la ventana

    # Listbox para mostrar los productos disponibles
    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Obtener y mostrar la lista de productos desde la base de datos
    prod_list = producto_db.ver_productos()  # Recuperar datos de productos
    for prd in prod_list:
        # Mostrar ID, nombre y descripción en el Listbox
        listbox.insert(tk.END, f"ID: {prd[0]}   |    Nombre: {prd[1]}   |   Precio: ${prd[3]}   |   Stock: {prd[4]}  |  Vendidos: {prd[5]}")

    def actualizar_producto():
        # Verificar que se haya seleccionado un producto
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Producto", "Debe seleccionar un producto para editar.")
            return

        # Obtener el ID del producto seleccionado
        producto_id = prod_list[seleccion[0]][0]

        # Recuperar los datos actuales del producto desde la base de datos
        producto_actual = producto_db.ver_producto(producto_id)[0]

        # Crear ventana para editar los datos del producto seleccionado
        actualizacion_window = tk.Toplevel()
        actualizacion_window.title("Editar datos del producto")
        actualizacion_window.geometry("500x400")  # Dimensiones
        actualizacion_window.resizable(False, False)  # Deshabilitar cambio de tamaño

        # Configurar las columnas de la cuadrícula para ajustar el ancho
        actualizacion_window.grid_columnconfigure(0, weight=1)  # Columna de etiquetas
        actualizacion_window.grid_columnconfigure(1, weight=3)  # Columna de entradas

        # Crear campos de entrada para cada atributo del producto
        tk.Label(actualizacion_window, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        nombre_entry = tk.Entry(actualizacion_window)
        nombre_entry.insert(0, producto_actual[1])  # Insertar el nombre actual
        nombre_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_window, text="Descripcion:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        descripcion_entry = tk.Entry(actualizacion_window)
        descripcion_entry.insert(0, producto_actual[2])  # Insertar la descripción actual
        descripcion_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_window, text="Precio:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        precio_entry = tk.Entry(actualizacion_window)
        precio_entry.insert(0, producto_actual[3])  # Insertar el precio actual
        precio_entry.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        tk.Label(actualizacion_window, text="Stock?:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        stock_entry = tk.Entry(actualizacion_window)
        stock_entry.insert(0, producto_actual[4])  # Insertar el stock actual
        stock_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")
    
        def validar_datos():
            """
            Valida los datos ingresados en los campos de entrada.
            """
            nombre = nombre_entry.get().strip()
            descripcion = descripcion_entry.get().strip()
            precio = precio_entry.get().strip()
            stock = stock_entry.get().strip()

            # Validar que los campos no estén vacíos y sean correctos
            if not nombre:
                messagebox.showerror("Error de Validación", "El nombre no puede estar vacío.")
                return False
            if not descripcion:
                messagebox.showerror("Error de Validación", "La descripción no puede estar vacía.")
                return False
            if not precio.replace('.', '', 1).isdigit():
                messagebox.showerror("Error de Validación", "El precio debe ser un número válido.")
                return False
            if not stock.isdigit():
                messagebox.showerror("Error de Validación", "El stock debe ser un número entero.")
                return False

            return True

        def guardar_cambios():
            """
            Guarda los cambios del producto en la base de datos si los datos son válidos.
            """
            if validar_datos():  # Validar datos antes de guardar
                nombre = nombre_entry.get()
                descripcion = descripcion_entry.get()
                precio = float(precio_entry.get())
                stock = int(stock_entry.get())

                # Actualizar el producto en la base de datos
                producto_db.actualizar_producto(producto_id, nombre, descripcion, precio, stock)
                messagebox.showinfo("Éxito", "El producto se ha actualizado con éxito.")
                actualizacion_window.destroy()  # Cerrar la ventana de edición

        # Botón para guardar los cambios, centrado en la ventana
        guardar_btn = tk.Button(actualizacion_window, text="Guardar Cambios", command=guardar_cambios)
        guardar_btn.grid(row=5, column=0, columnspan=2, pady=20)

    # Botón principal para abrir la ventana de edición
    tk.Button(window, text="Actualizar producto Seleccionado", command=actualizar_producto).pack(pady=10)
