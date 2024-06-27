CREATE DATABASE empresa;
USE empresa;
CREATE TABLE `empresa`.`clientes` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , `email` VARCHAR(255) NOT NULL , `telefono` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;
CREATE USER 'josevicente'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';GRANT USAGE ON *.* TO 'josevicente'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;GRANT ALL PRIVILEGES ON `empresa`.* TO 'josevicente'@'localhost';