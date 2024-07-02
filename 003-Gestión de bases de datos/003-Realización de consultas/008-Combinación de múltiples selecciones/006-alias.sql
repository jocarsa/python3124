SELECT 
pedidos.fecha AS 'fecha del pedido',
pedidos.idpedido AS 'Numero del pedido',
clientes.nombre AS 'Nombre del cliente',
clientes.apellidos AS 'Apellidos del cliente',
productos.nombre AS 'Nombre del producto',
categorias.nombre AS 'Categoría del producto',
pedidos.unidades AS 'Unidades',
productos.precio AS 'Precio por unidad',
pedidos.unidades*productos.precio AS 'Total pedido en euros'

FROM `pedidos` 
LEFT JOIN clientes ON pedidos.clientes_nombre = clientes.Identificador
LEFT JOIN productos ON pedidos.productos_nombre = productos.Identificador
LEFT JOIN categorias ON productos.categorias_nombre = categorias.Identificador