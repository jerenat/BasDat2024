from models.conexion import BaseDeDatos

class Cliente:
    def __init__(self, db):
        self.db = db

    def registrar_cliente(self, nombre, apellido, telefono, email, direccion):
        query = "INSERT INTO Clientes (nombre, apellido, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, telefono, email, direccion)
        self.db.ejecutar(query, valores)
        return "Cliente registrado con éxito."

    def actualizar_cliente(self, cliente_id, nombre, apellido, telefono, email, direccion):
        query = "UPDATE Clientes SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s WHERE cliente_id=%s"
        valores = (nombre, apellido, telefono, email, direccion, cliente_id)
        self.db.ejecutar(query, valores)
        return "Cliente actualizado con éxito."

    def ver_cliente(self, cliente_id):
        query = "SELECT * FROM Clientes WHERE cliente_id = %s"
        return self.db.obtener_datos(query, (cliente_id,))
        
    def eliminar_cliente(self, cliente_id):
        query = "DELETE FROM Clientes WHERE cliente_id = %s"
        self.db.ejecutar(query, (cliente_id,))
        return "Cliente eliminado con éxito."

    def ver_clientes(self):
        query = "SELECT * FROM Clientes ORDER BY cliente_id ASC"
        return self.db.obtener_datos(query)
        
    def buscar_cliente_por_nombre(self, nombre):
        query = "SELECT * FROM Clientes WHERE nombre LIKE %s"
        valores = (f"%{nombre}%",)  # La coma convierte esto en una tupla
        return self.db.obtener_datos(query, valores)
