# **PROYECTO FINAL - BASES DE DATOS I**

## **Ejercicio: Sistema de Ventas Online**

El objetivo es crear una plataforma de ventas en línea para gestionar productos, clientes y órdenes de compra. Las órdenes deben incluir detalles como el producto, la fecha de pedido y la cantidad de unidades.

---

### **Modelo del Sistema**
- **Entidades principales**: **Productos**, **Clientes** y **Órdenes**.
- **Datos iniciales**: 
  - Al menos 10 productos.
  - Al menos 10 clientes.
  - Cada cliente debe tener un promedio de 10 órdenes.

---

## **Consignas**

1. **Gestión de Productos**:  
   - Agregar, actualizar, visualizar y eliminar productos.  
   - Incluir categorías y niveles de stock.
2. **Gestión de Clientes**:  
   - Registrar, actualizar y visualizar detalles de clientes.  
   - Gestionar información de contacto.
3. **Procesamiento de Órdenes**:  
   - Visualizar órdenes asociadas a un cliente específico.
4. **Búsquedas Avanzadas**:  
   - Filtrar productos o clientes, por ejemplo, productos más vendidos.
5. **Reporte de Productos Más Vendidos**:  
   - Generar un informe con el producto más vendido y la cantidad total pedida.
6. **Modificación de Cantidad de Productos**:  
   - Ajustar las órdenes de un producto para limitar la cantidad máxima pedida.

---

## **Esquema de Base de Datos**

El diseño cumple con la **Tercera Forma Normal (3FN)** para evitar redundancias y garantizar la integridad de los datos.

### Tablas:
- **Clientes**:  
  `cliente_id, nombre, apellido, telefono, email, direccion`
- **Productos**:  
  `idproducto, nombre, descripcion, precio, stock, vendidos`
- **Órdenes**:  
  `orden_id, producto_id, cliente_id, cantidad, fecha_pedido`

---

## **Claves Candidatas**

- **Clientes**: Clave primaria → `cliente_id`
- **Productos**: Clave primaria → `idproducto`
- **Órdenes**: Clave primaria → `orden_id`

---

## **Normalización**

### Primera Forma Normal (1FN)
- Las tablas no contienen atributos multivaluados ni repetidos.

### Segunda Forma Normal (2FN)
- Todos los atributos no clave dependen completamente de la clave primaria.

### Tercera Forma Normal (3FN)
- **Clientes**: Todos los atributos dependen directamente de `cliente_id`.
- **Productos**: No hay dependencias funcionales transitivas, todos los atributos dependen de `idproducto`.
- **Órdenes**: Todos los atributos dependen directamente de `orden_id`.

---

## **Estructura de Directorios**

```plaintext
/components:    Contiene las interfaces gráficas (ejemplo: gui_client.py).
/context:       Contiene objetos para la conexión con la base de datos.
/models:        Incluye el archivo `conexion.py` para gestionar la base de datos.
/images:        Almacena imágenes usadas en el menú.
```

---

## **Funcionamiento del Proyecto**

El archivo principal `app.py` coordina el funcionamiento del proyecto y conecta con otros archivos:

### Archivos Python:
- **Interfaces Gráficas**:  
  `gui_client.py`, `gui_ventas.py`, `gui_ordenes.py`, `gui_acerca.py`
- **Conexión con la Base de Datos**:  
  `models/conexion.py` gestiona la conexión y operaciones CRUD.
- **Gestión de Entidades**:  
  - `context/clientes.py` → Clientes  
  - `context/productos.py` → Productos  
  - `context/ordenes.py` → Órdenes  

### Archivo SQL:
- **`basededatosi.sql`**:  
  Contiene las estructuras SQL y datos iniciales.
