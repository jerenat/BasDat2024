import tkinter as tk
from tkinter import messagebox

def mostrar_eliminacion_cliente(cliente_db):
    ventana = tk.Toplevel()
    ventana.geometry("640x480+500+300")
    ventana.resizable(False, False)
    ventana.title("Eliminar Cliente(s)")

    listbox = tk.Listbox(ventana)
    listbox.pack(fill=tk.BOTH, expand=True)

    clientes = cliente_db.ver_clientes()
    for cliente in clientes:
        listbox.insert(tk.END, f"{cliente[0]} - {cliente[1]} {cliente[2]}")

    def eliminar_cliente():
        seleccion = listbox.curselection()


        if not seleccion:
            messagebox.showwarning("Seleccionar Cliente", "Debe seleccionar un cliente para eliminar.")
            return
        

        cliente_id = clientes[seleccion[0]][0]

        
        # Confirmación previa
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar el Cliente seleccionado?\n\nID: {cliente_id}\nNombre: {clientes[seleccion[0]][1]}"
        )

        if confirmacion:
            cliente_db.eliminar_cliente(cliente_id)
            messagebox.showinfo("Éxito", "Cliente eliminado con éxito.")
            listbox.delete(seleccion)
        else:
            messagebox.showinfo("Cancelado", "Cancelado por el usuario.")

    tk.Button(ventana, text="Eliminar Cliente Seleccionado", command=eliminar_cliente, bd=1).pack(pady=10)
