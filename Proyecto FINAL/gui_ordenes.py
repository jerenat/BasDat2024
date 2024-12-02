import tkinter as tk


from components.ver_ordenes import mostrar_ordenes_cliente
from components.registrar_ordenes import mostrar_registro_ordenes


def mostrar_gestion_ordenes(cliente_db, producto_db, ordenes_db):

    root = tk.Tk()
    root.geometry("720x130")
    root.resizable(False, False)
    root.title("Gestión de Ordenes")

    root.grid_columnconfigure(0, weight=1)

    # Botones con sus respectivas funciones
    tk.Button(root, text="Registrar Nueva Orden", padx=20, pady=10, bd=1, command=lambda: mostrar_registro_ordenes(cliente_db, producto_db, ordenes_db)).grid(row=0, column=0, sticky="ew", padx=15, pady=5)

    tk.Button(root, text="Ver Ordenes por Clientes (Incluye Editar / Eliminar)", padx=20, pady=10, bd=1, command=lambda: mostrar_ordenes_cliente(cliente_db, ordenes_db)).grid(row=1, column=0, sticky="ew", padx=15, pady=5)



    root.mainloop()