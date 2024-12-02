import tkinter as tk

def mostrar_acerca_de():
    root = tk.Tk()
    root.geometry("450x250+620+400")
    root.resizable(False, False)
    root.title("Acerca de Sistema de Ventas v0.0.1")

    # Configurar las filas y columnas para expandirse
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)


    tk.Label(
        root,
        text="Acerca de Sistema de Ventas v0.0.1",
        font=("Arial", 17),
        justify="center"
    ).grid(row=1, column=0, sticky="nsew", pady=10)
    
    tk.Label(
        root,
        text=(
            "Un simple sistema de ventas para la gestión y administración "
            "de productos, órdenes y clientes desarrollado como proyecto para "
            "'Bases de Datos 1'. (c) 2024 - Todos los derechos reservados."
        ),
        font=("Arial", 12),
        wraplength=400,  # Limitar el ancho a 400 píxeles
        justify="center"
    ).grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

    root.mainloop()
