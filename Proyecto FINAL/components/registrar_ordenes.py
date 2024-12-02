import tkinter as tk
from tkinter import messagebox

def mostrar_registro_ordenes(cliente_db, producto_db, ordenes_db):
    # Crear ventana principal
    window = tk.Toplevel()
    window.geometry("640x480+500+300")
    window.resizable(False, False)
    window.title("Registro de Nuevas Ordenes")

    # Listbox para mostrar productos
    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Obtener lista de productos
    prod_list = producto_db.ver_productos()
    for prd in prod_list:
        listbox.insert(tk.END, f"ID: {prd[0]}   |    Nombre: {prd[1]}   |   Precio: ${prd[3]}   |   Stock: {prd[4]}  |  Vendidos: {prd[5]}")

    # -- Función para generar la orden de un usuario --
    def generar_usuarios():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Producto", "Debe seleccionar un producto para Generar la Orden.")
            return

        # Obtener el ID del producto seleccionado
        producto_id = prod_list[seleccion[0]][0]

        # Crear ventana para registrar la orden
        actualizacion_window = tk.Toplevel()
        actualizacion_window.title("Generar Orden de Usuario")
        actualizacion_window.geometry("500x300")
        actualizacion_window.resizable(False, False)
        actualizacion_window.grid_columnconfigure(0, weight=1)
        actualizacion_window.grid_columnconfigure(1, weight=3)

        # -- USUARIOS REGISTRADOS --
        tk.Label(actualizacion_window, text=" --- Usuarios Registrados ---", font=("Arial", 13, "bold")).grid(row=0, column=0)

        # Crear una variable StringVar para el valor seleccionado
        usuarios_registrados = tk.StringVar()

        # Obtener la lista de clientes
        clientes = cliente_db.ver_clientes()
        opciones = [(f"{cliente[1]} {cliente[2]}", cliente[0]) for cliente in clientes]

        if opciones:
            usuarios_registrados.set("Seleccione una Opcion")

        # Función para obtener el id del cliente seleccionado
        def obtener_seleccion():
            nombre_seleccionado = usuarios_registrados.get()
            return next((cliente_id for nombre, cliente_id in opciones if nombre == nombre_seleccionado), None)

        # Crear el OptionMenu con los clientes registrados
        menu_registrados = tk.OptionMenu(actualizacion_window, usuarios_registrados, *[opcion[0] for opcion in opciones])
        menu_registrados.config(bd=1)
        menu_registrados.grid(row=1, column=0, sticky="ew", padx=15, pady=10)

        # -- CANTIDAD DE PRODUCTOS --
        tk.Label(actualizacion_window, text=" --- Producto ---", font=("Arial", 13, "bold")).grid(row=2, column=0, pady=10)
        tk.Label(actualizacion_window, text="Cantidad:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        cantidad_entry = tk.Entry(actualizacion_window)
        cantidad_entry.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky="ew")

        # -- BOTON PARA FINALIZAR Y REGISTRAR LA ORDEN --
        def finalizar_orden():
            # Validaciones
            if usuarios_registrados.get() == "Seleccione una Opcion" or not usuarios_registrados.get():
                messagebox.showerror("Error", "Debe seleccionar un usuario.")
                return

            cantidad = cantidad_entry.get()
            if not cantidad.isdigit() or int(cantidad) < 1:
                messagebox.showerror("Error", "La cantidad debe ser un número mayor o igual a 1.")
                return

            cliente_id = obtener_seleccion()
            cantidad = int(cantidad)

            # Registrar la orden
            ordenes_db.registrar_orden(producto_id, cliente_id, cantidad)

            messagebox.showinfo("Éxito", "Orden Generada Satisfactoriamente")
            actualizacion_window.destroy()
            window.destroy()

        # Botón para finalizar la orden
        boton_mostrar = tk.Button(actualizacion_window, text="Finalizar Orden Ahora", command=finalizar_orden, bd=1)
        boton_mostrar.grid(row=4, column=0, pady=20)

    # Botón para abrir la ventana de edición
    tk.Button(window, text="Generar Orden Ahora", command=generar_usuarios, bd=1).pack(pady=10)

    # Mostrar la ventana principal
    window.mainloop()
