import tkinter as tk
from tkinter import messagebox


def mostrar_ordenes_cliente(cliente_db, ordenes_db):
    # Ventana principal para mostrar clientes
    ventana = tk.Toplevel()
    ventana.geometry("640x480+500+300")
    ventana.resizable(False, False)
    ventana.title("Ver órdenes del cliente")

    # Listbox para listar clientes
    listbox = tk.Listbox(ventana)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Recuperar y mostrar clientes desde la base de datos
    clientes = cliente_db.ver_clientes()
    for cliente in clientes:
        listbox.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]}")  # ID, nombre y apellido

    def ver_ordenes_id():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Seleccionar Cliente", "Debe seleccionar un cliente para ver sus órdenes.")
            return

        cliente_id = clientes[seleccion[0]][0]

        # Ventana para mostrar las órdenes del cliente seleccionado
        ord_ventana = tk.Toplevel()
        ord_ventana.geometry("640x480+500+300")
        ord_ventana.resizable(False, False)
        ord_ventana.title("Órdenes del cliente")

        # Listbox para listar órdenes
        ord_listbox = tk.Listbox(ord_ventana)
        ord_listbox.pack(fill=tk.BOTH, expand=True)

        # Recuperar y mostrar órdenes del cliente desde la base de datos
        ordenes = ordenes_db.ver_orden_por_cliente(cliente_id)
        for orden in ordenes:
            ord_listbox.insert(tk.END, f"{orden[0]} - {orden[1]} ({orden[2]})")  # ID, producto, cantidad

        # Función para editar la orden seleccionada
        def editar_orden_seleccionada():
            seleccion = ord_listbox.curselection()
            if not seleccion:
                messagebox.showwarning("Error", "Debe seleccionar una orden para editar.")
                return

            orden_id = ordenes[seleccion[0]][0]
            orden_actual = ordenes_db.ver_orden_por_id(orden_id)[0]

            # Ventana para editar la orden
            edit_window = tk.Toplevel()
            edit_window.geometry("400x160+600+500")
            edit_window.resizable(False, False)
            edit_window.title("Editar orden")

            # Configuración de etiquetas y entradas
            tk.Label(edit_window, text="Stock actual:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
            stock_entry = tk.Entry(edit_window)
            stock_entry.insert(0, orden_actual[4])  # Stock actual
            stock_entry.grid(row=0, column=1, padx=10, pady=10)

            tk.Label(edit_window, text=f"Stock máximo: {orden_actual[5]}", fg="red").grid(row=0, column=2, padx=10, pady=10)

            # Función para guardar la orden editada
            def guardar_cambios():
                nuevo_stock = stock_entry.get()
                if not nuevo_stock.isdigit():
                    messagebox.showerror("Error", "Debe ingresar un stock válido.")
                    return

                nuevo_stock = int(nuevo_stock)
                if nuevo_stock > orden_actual[5]:
                    messagebox.showerror("Error", "El stock excede el máximo permitido.")
                    return

                ordenes_db.actualizar_orden(orden_id, nuevo_stock)
                messagebox.showinfo("Éxito", "La orden fue actualizada con éxito.")
                edit_window.destroy()

            # Botón para guardar los cambios
            tk.Button(edit_window, text="Guardar Orden Editada", command=guardar_cambios, bd=1).grid(row=1, column=0, columnspan=3, pady=20)

        # Función para eliminar la orden seleccionada
        def eliminar_orden_seleccionada():
            seleccion = ord_listbox.curselection()
            if not seleccion:
                messagebox.showwarning("Error", "Debe seleccionar una orden para eliminar.")
                return

            orden_id = ordenes[seleccion[0]][0]
            confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de eliminar la orden {orden_id}?")
            if confirmacion:
                ordenes_db.eliminar_orden(orden_id)
                ord_listbox.delete(seleccion)
                messagebox.showinfo("Éxito", "La orden fue eliminada.")

        # Botones para editar y eliminar
        tk.Button(ord_ventana, text="Editar Orden", command=editar_orden_seleccionada, bd=1).pack(pady=10)
        tk.Button(ord_ventana, text="Eliminar Orden", command=eliminar_orden_seleccionada, bd=1).pack(pady=10)

    # Botón para ver órdenes del cliente seleccionado
    tk.Button(ventana, text="Ver órdenes", command=ver_ordenes_id, bd=1).pack(pady=10)
