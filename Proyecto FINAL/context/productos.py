from models.conexion import BaseDeDatos


class Producto:
    def __init__(self, db):
        self.db = db

    # -- INSERTAR PRODUCTO
    def registrar_producto(self, nombre, descripcion, precio, stock):
        query = "INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
        valores = (nombre, descripcion, precio, stock)
        self.db.ejecutar(query, valores)
        return "Producto registrado con éxito."


    # -- EDITAR PRODUCTO
    def actualizar_producto(self, producto_id, nombre, descripcion, precio, stock):
        query = "UPDATE Productos SET nombre=%s, descripcion=%s, precio=%s, stock=%s WHERE idproducto=%s"
        valores = (nombre, descripcion, precio, stock, producto_id)
        self.db.ejecutar(query, valores)
        return "Producto actualizado con éxito."


    # -- VER PRODUCTO
    def ver_productos(self):
        query = "SELECT * FROM Productos"
        return self.db.obtener_datos(query)
       
    # -- VER PRODUCTO POR ID
    def ver_producto(self, producto_id):
        query = "SELECT * FROM Productos WHERE idproducto = %s"
        return self.db.obtener_datos(query, (producto_id,))


    # -- ELIMINAR PRODUCTO  
    def eliminar_producto(self, producto_id):
        query = "DELETE FROM Productos WHERE idproducto = %s"
        self.db.ejecutar(query, (producto_id,))
        return "Producto eliminado con éxito."
    

    # -- VER PRODUCTO POR NOMBRE
    def buscar_producto_por_nombre(self, nombre, vendidos_filtro=False):
        query = "SELECT * FROM Productos WHERE nombre LIKE %s"
        valores = (f"%{nombre}%",)
        
        if vendidos_filtro:
            # Ordenar por los más vendidos
            query += " ORDER BY vendidos DESC"
        
        return self.db.obtener_datos(query, valores)
