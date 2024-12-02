import tkinter as tk
from tkinter import messagebox, ttk

def eliminar_productos(producto_db):
    window = tk.Toplevel()
    window.geometry("640x480+500+300")
    window.resizable(False, False)
    window.title("Eliminar producto(s)")

    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Mostrar en DDBB los datos del producto
    prod_list = producto_db.ver_productos()

    for prd in prod_list:
        listbox.insert(tk.END, f"ID: {prd[0]}   |    Nombre: {prd[1]}   |   Precio: ${prd[3]}   |   Stock: {prd[4]}  |  Vendidos: {prd[5]}")

    def eliminar_producto():
        seleccion = listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Error al seleccionar producto", "Debes seleccionar un producto para eliminar.")
            return

        producto_id = prod_list[seleccion[0]][0]

        # Confirmación previa
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar el producto seleccionado?\n\nID: {producto_id}\nNombre: {prod_list[seleccion[0]][1]}"
        )

        if confirmacion:
            producto_db.eliminar_producto(producto_id)
            messagebox.showinfo("Éxito", "Producto eliminado con éxito.")
            listbox.delete(seleccion)
        else:
            messagebox.showinfo("Cancelado", "Eiminación cancelada por el Usuario.")

    tk.Button(window, text="Eliminar producto seleccionado", command=eliminar_producto).pack(pady=10)
