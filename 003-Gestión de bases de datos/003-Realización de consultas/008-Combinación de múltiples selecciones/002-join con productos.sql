SELECT 
pedidos.fecha,
pedidos.idpedido,
clientes.nombre,
clientes.apellidos
FROM `pedidos` 
LEFT JOIN clientes ON pedidos.clientes_nombre = clientes.Identificador