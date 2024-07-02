CREATE TABLE `empresa`.`categorias` (`Identificador` INT(255) NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(255) NOT NULL , PRIMARY KEY (`Identificador`)) ENGINE = InnoDB;

INSERT INTO `categorias` (`Identificador`, `nombre`) VALUES (NULL, 'Agua con gas');

INSERT INTO `categorias` (`Identificador`, `nombre`) VALUES (NULL, 'Agua sin gas');