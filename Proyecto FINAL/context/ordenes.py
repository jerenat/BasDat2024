from models.conexion import BaseDeDatos
from datetime import datetime

class Ordenes:
    def __init__(self, db):
        self.db = db

    def registrar_orden(self, producto_id, cliente_id, cantidad):


        fecha_pedido = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formato compatible con MySQL
        
        query = "INSERT INTO ordenes (producto_id, cliente_id, cantidad, fecha_pedido) VALUES (%s, %s, %s, %s)"
        valores = (producto_id, cliente_id, cantidad, fecha_pedido)
        self.db.ejecutar(query, valores)
        return "Orden registrada con éxito."
    




    def actualizar_orden(self, orden_id, cantidad):
        query = "UPDATE ordenes SET cantidad=%s WHERE orden_id=%s"
        valores = (cantidad, orden_id)
        self.db.ejecutar(query, valores)
        return "Orden actualizada con éxito."


    def ver_orden_por_id(self, orden_id):
        query = """
        SELECT o.orden_id, o.fecha_pedido, p.nombre, p.precio, o.cantidad, p.stock
        FROM ordenes AS o
        INNER JOIN productos AS p ON o.producto_id = p.idproducto
        WHERE o.orden_id = %s
        ORDER BY o.fecha_pedido DESC
        """
        return self.db.obtener_datos(query, (orden_id,))


    def ver_orden_por_cliente(self, cliente_id):
        query = """
        SELECT o.orden_id, o.fecha_pedido, p.nombre, p.precio, o.cantidad
        FROM ordenes AS o
        INNER JOIN productos AS p ON o.producto_id = p.idproducto
        WHERE o.cliente_id = %s
        ORDER BY o.fecha_pedido DESC
        """
        return self.db.obtener_datos(query, (cliente_id,))

    def eliminar_orden(self, orden_id):
        query = "DELETE FROM ordenes WHERE orden_id = %s"
        self.db.ejecutar(query, (orden_id,))
        return "Orden eliminada con éxito."

    def ver_ordenes(self):
        query = "SELECT * FROM ordenes"
        return self.db.obtener_datos(query)
        
    def buscar_orden_por_id(self, orden_id):
        query = "SELECT * FROM ordenes WHERE orden_id LIKE %s"
        valores = (f"%{orden_id}%",)  # La coma convierte esto en una tupla
        return self.db.obtener_datos(query, valores)
