ALTER TABLE `productos` ADD `categorias_nombre` INT(255) NOT NULL AFTER `precio`;

ALTER TABLE `productos` ADD CONSTRAINT `categoriasnombre` FOREIGN KEY (`categorias_nombre`) REFERENCES `categorias`(`Identificador`) ON DELETE RESTRICT ON UPDATE RESTRICT;