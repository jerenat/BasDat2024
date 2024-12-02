-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 02-12-2024 a las 04:08:40
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basededatosi`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `cliente_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`cliente_id`),
  UNIQUE KEY `email` (`email`),
  KEY `idx_cliente_email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`cliente_id`, `nombre`, `apellido`, `telefono`, `email`, `direccion`, `fecha_registro`) VALUES
(14, 'Abigail', 'Ibañez', '2932553759', 'abigailibanez19401@gmail.com', 'Cervantes 30', NULL),
(11, 'Ismael', 'Lopez', '2914352532', 'ismael8887@gmail.com', 'Independencia 3530', NULL),
(12, 'Sergio', 'Ramirez', '2915035948', 'sergioramirez@gmail.com', 'Islas Orcadas 1084', NULL),
(4, 'María', 'Martínez', '2915660070', 'maria.martinez@example.com', 'Calle de la Amargura 111', NULL),
(5, 'Luis', 'Fernández', '2945558764', 'luis.fernandez@example.com', 'Paseo de la Paz 101', NULL),
(6, 'Laura', 'Gómez', '1135552345', 'laura.gomez@example.com', 'Callejón del Beso 202', NULL),
(13, 'Holy', 'Rawson', '2932553647', 'holyrawson1323@outlook.com', 'Harris 332', NULL),
(8, 'Sofía', 'Ramírez', '1135554567', 'sofia.ramirez@example.com', 'Pasaje del Viento 404', NULL),
(9, 'Ricardo', 'Castro', '1145555678', 'ricardo.castro@example.com', 'Boulevard de los Sueños 505', NULL),
(10, 'Lucía', 'Domínguez', '3875556789', 'lucia.dominguez@example.com', 'Calle Luna 606', NULL),
(15, 'Isaac', 'Jacob', '1173324854', 'isaacjacob@citromail.hu', 'Alsina 35, Piso 3', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenes`
--

DROP TABLE IF EXISTS `ordenes`;
CREATE TABLE IF NOT EXISTS `ordenes` (
  `orden_id` int NOT NULL AUTO_INCREMENT,
  `producto_id` int DEFAULT NULL,
  `cliente_id` int DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `fecha_pedido` datetime DEFAULT NULL,
  PRIMARY KEY (`orden_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `ordenes`
--

INSERT INTO `ordenes` (`orden_id`, `producto_id`, `cliente_id`, `cantidad`, `fecha_pedido`) VALUES
(11, 17, 4, 1, '2024-12-02 01:02:21'),
(10, 15, 4, 1, '2024-12-02 01:01:29'),
(9, 18, 4, 3, '2024-12-02 01:01:07'),
(8, 9, 4, 8, '2024-12-02 01:00:08'),
(7, 5, 4, 1, '2024-12-02 00:59:51'),
(12, 21, 4, 4, '2024-12-02 01:03:43'),
(13, 14, 4, 5, '2024-12-02 01:04:36'),
(14, 6, 4, 2, '2024-12-02 01:04:50'),
(15, 19, 4, 8, '2024-12-02 01:05:12'),
(16, 10, 4, 1, '2024-12-02 01:05:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `idproducto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `descripcion` text,
  `precio` varchar(255) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `vendidos` int DEFAULT NULL,
  PRIMARY KEY (`idproducto`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`idproducto`, `nombre`, `descripcion`, `precio`, `stock`, `vendidos`) VALUES
(5, 'Notebook Lenovo', 'Notebook Lenovo G12, 1tb de SSD, 18gb de RAM', '16000.0', 12, 15428),
(6, 'Auriculares TWS-6', 'Auriculares TWS-6, 9\" con Bluetooth 5.1, Bateria de 500mAh', '7500.0', 100, 2843),
(7, 'Movil Xiaomi Redmi Mi 11', 'Xiaomi Redmi Note 11, 128gb de ROM, 4gb de RAM, Camara: 50mpx', '230000.0', 35, 483),
(8, 'Televisor LG 45 pulgadas', 'Televidor LG 45\", WebOS 4.0, Magic Mouse, Bluetooth 5.1, Parlantes Stereo 9x6\"', '450000.0', 10, 3830),
(9, 'Tablet Lenovo 7 pulgadas', 'Tablet Lenovo 7\" , 64gb de ROM, 8gb de RAM, Android 13', '75000.0', 23, 3405),
(10, 'Nintendo Switch + 100 Juegos', 'Nintendo Switch + 100 Juegos incluidos, 1tb de ROM, 16gb de RAM', '500000.0', 8, 1224),
(11, 'Smartwatch Samsung Fold 5', 'Smartwatch Samsung Fold 5, Pantalla: 3\", Android 9, 64gb de RAM', '45500.0', 150, 4596),
(12, 'Samsung Galaxy Z- Fold 4', 'Samsung Galaxy Z-Fold 4, 256gb de ROM, 16gb de RAM, Camara: 200mpx, Android: 15, Stylus', '1300000.0', 18, 3543),
(13, 'Apple Macbook 2023', 'Apple Macbook 2023, 2tb de M.2, Procesador L2, 64gb de RAM, macOS 19.10', '2500000.0', 9, 9879),
(14, 'Placa de Desarrollo Raspberry Pi 5w', 'Placa Raspberry Pi 5 + Wifi + Bluetooth + Micro SD 128gb', '45700.0', 89, 3943),
(15, 'Cable HDMI 25 Metros', 'Cable HDMI 25 metros reforzado', '9600.0', 24, 222),
(16, 'Gabinete ASUS', 'Gabinete PC ASUS + LEDS Reprogramables', '89600.0', 18, 5543),
(17, 'Monitor LG 19 pulgadas', 'Monitor LG 19\", Pantalla IPS + Protector de Retina', '95750.0', 88, 406),
(18, 'Reprogramador de BIOS CH341A', 'Reprogramador de BIOS CH341A + Pinza metálica + Software BIOS', '18670.0', 45, 11),
(19, 'Auto electrico juguete', 'Auto electrico juguete Infrarojo + Control inalambrico + 3 pilas AAA', '67500.0', 28, 3524),
(20, 'Notebook EXO 15.6 pulgadas', 'Notebook EXO 15.6\", 2tb de ROM, 16gb de RAM, Intel Core i5', '385020.0', 324, 3456),
(21, 'Router TP-LINK Aginet', 'Router TP-LINK Aginet 4 antenas, 12v 1A + Manual', '75000.0', 88, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
