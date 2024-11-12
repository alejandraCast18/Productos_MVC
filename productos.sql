
-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 12-06-2023 a las 03:43:23
-- Versión del servidor: 10.10.2-MariaDB
-- Versión de PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base_datos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `id_pro` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID del producto',
  `cod_pro` char(10) NOT NULL COMMENT 'Código del producto',
  `nom_pro` varchar(20) NOT NULL COMMENT 'Nombre del producto',
  `mod_pro` varchar(20) NOT NULL COMMENT 'Modelo del producto',
  `pre_pro` decimal(12,2) NOT NULL COMMENT 'Precio del producto',
  `can_pro` smallint(50) UNSIGNED NOT NULL COMMENT 'Cantidad del producto',
  PRIMARY KEY (`id_pro`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_pro`, `cod_pro`, `nom_pro`, `mod_pro`, `pre_pro`, `can_pro`) VALUES
(1, 'RES001', 'RESISTENCIA', 'RV', '2.00', 222),
(2, 'TRAS-11', 'TRANSISTOR', 'PNP', '1.00', 554),
(3, '10101', 'CONDENSADOR', 'CERAMICO', '2.00', 100),
(4, 'DB121', 'DIODO', 'ZENER', '1.50', 231),
(5, 'IC002', 'IC', 'AND', '1.00', 200),
(6, 'IC003', 'IC', 'XOR', '1.00', 300),
(7, 'D0092', 'DIOD0', 'ZENER', '2.00', 232),
(8, 'RE21', 'RELE', '221R', '2.50', 423),
(9, '2560', 'ARDUINO', 'MEGA', '30.00', 37),
(10, '2021DS', 'ARDUINO', 'UNO R3', '15.50', 73),
(11, 'RES2021', 'RESISTENCIA', '4B', '0.10', 1000),
(12, 'LED122', 'LED', 'GREENR3', '0.50', 144),
(13, 'LDR43', 'LDR', 'LDRG', '2.00', 43),
(14, 'FUSI232', 'FUSIBLE', '23FDEW', '2.00', 331),
(15, 'MATRIZ32', 'MATRIZ', '32X8', '50.00', 56),
(16, 'SENSORRE', 'ULTRASONIC', 'RGR0544', '5.00', 231),
(17, '555N', 'TIMER', '555', '1.50', 621),
(18, 'ER43', 'PILAS', 'AAA', '2.00', 544),
(19, '1212', '12121', '12121', '22121.00', 12121);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
