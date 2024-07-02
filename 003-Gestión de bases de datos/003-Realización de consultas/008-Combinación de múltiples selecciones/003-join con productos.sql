SELECT 
pedidos.fecha,
pedidos.idpedido,
clientes.nombre,
clientes.apellidos,
productos.nombre,
productos.precio
FROM `pedidos` 
LEFT JOIN clientes ON pedidos.clientes_nombre = clientes.Identificador
LEFT JOIN productos ON pedidos.productos_nombre = productos.Identificador