# **Ejercicio 4 - Trabajo Práctico 5**  
## **Diseño de la Base de Datos para Talleres de Autos**  
**Autor:** Jeremías Geminiani  

---

## **Dependencias Funcionales (DFs)**  

- **`codigoSucursal → domicilioSucursal, telefonoSucursal`**  
  Cada `codigoSucursal` identifica de forma única el domicilio y el teléfono de una sucursal.  

- **`codigoSucursal, codigoFosa → largoFosa, anchoFosa`**  
  La combinación de `codigoSucursal` y `codigoFosa` determina las dimensiones de una fosa específica.  

- **`codigoSucursal, codigoFosa, patenteAuto → marcaAuto, modeloAuto, dniCliente`**  
  Este conjunto define el auto reparado en una fosa específica de una sucursal, junto con el cliente propietario.  

- **`patenteAuto → marcaAuto, modeloAuto, dniCliente`**  
  La `patenteAuto` identifica de manera única un auto, incluyendo su marca, modelo y cliente propietario.  

- **`dniCliente → nombreCliente, celularCliente`**  
  El `dniCliente` permite obtener de forma única el nombre y celular del cliente.  

- **`dniMecanico → nombreMecanico, emailMecanico`**  
  El `dniMecanico` identifica de manera única a un mecánico, proporcionando su nombre y correo electrónico.  

---

## **Claves Candidatas**  

La combinación de **`codigoSucursal, codigoFosa, patenteAuto`** permite identificar de manera única cada registro dentro del sistema, ya que incluye:  

- **`codigoSucursal`**: Identifica la sucursal.  
- **`codigoFosa`**: Especifica la fosa dentro de la sucursal.  
- **`patenteAuto`**: Identifica de manera única un auto.  

Por lo tanto, esta combinación es la clave candidata más adecuada.  

---

## **Clave Primaria**  

### **Clave primaria seleccionada:**  
`codigoSucursal, codigoFosa, patenteAuto`  

### **Justificación:**  
Esta clave refleja la estructura jerárquica del sistema, conectando sucursales, fosas y autos. Es la opción más representativa y funcional para identificar registros de manera precisa.  

---

## **Normalización**  

### **1FN - Primera Forma Normal**  
El esquema inicial ya cumple con la 1FN, ya que todos los atributos contienen valores atómicos y no hay repeticiones ni listas en los campos.  

---

### **2FN - Segunda Forma Normal**  
Para alcanzar la 2FN, se eliminaron dependencias parciales mediante la descomposición del esquema en las siguientes tablas:  

- **`Sucursal`**: `{codigoSucursal, domicilioSucursal, telefonoSucursal}`  
- **`Fosa`**: `{codigoSucursal, codigoFosa, largoFosa, anchoFosa}`  
- **`AutoCliente`**: `{codigoSucursal, codigoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente}`  
- **`Cliente`**: `{dniCliente, nombreCliente, celularCliente}`  
- **`Mecanico`**: `{dniMecanico, nombreMecanico, emailMecanico}`  
- **`Reparacion`**: `{codigoSucursal, codigoFosa, patenteAuto, dniMecanico}`  

---

### **3FN - Tercera Forma Normal**  
Para alcanzar la 3FN, se eliminaron dependencias transitivas, reorganizando los datos en tablas independientes.  

#### **Tabla Sucursal**  
- **`codigoSucursal`** (Clave primaria)  
- `domicilioSucursal`  
- `telefonoSucursal`  

#### **Tabla Fosa**  
- **`codigoSucursal`** (Clave foránea a Sucursal)  
- **`codigoFosa`** (Clave primaria compuesta junto con `codigoSucursal`)  
- `largoFosa`  
- `anchoFosa`  

#### **Tabla Auto**  
- **`patenteAuto`** (Clave primaria)  
- `marcaAuto`  
- `modeloAuto`  
- **`dniCliente`** (Clave foránea a Cliente)  

#### **Tabla Cliente**  
- **`dniCliente`** (Clave primaria)  
- `nombreCliente`  
- `celularCliente`  

#### **Tabla Mecanico**  
- **`dniMecanico`** (Clave primaria)  
- `nombreMecanico`  
- `emailMecanico`  

#### **Tabla Reparacion**  
- **`codigoSucursal`** (Clave foránea a Sucursal)  
- **`codigoFosa`** (Clave foránea a Fosa)  
- **`patenteAuto`** (Clave foránea a Auto)  
- **`dniMecanico`** (Clave foránea a Mecanico)  
- **Clave primaria compuesta:** (`codigoSucursal`, `codigoFosa`, `patenteAuto`, `dniMecanico`)  