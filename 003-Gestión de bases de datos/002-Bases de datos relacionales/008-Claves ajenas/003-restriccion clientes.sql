ALTER TABLE `pedidos` ADD CONSTRAINT `pedidosclientes` FOREIGN KEY (`clientes_nombre`) REFERENCES `clientes`(`Identificador`) ON DELETE RESTRICT ON UPDATE RESTRICT;