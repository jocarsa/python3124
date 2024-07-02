SELECT
categorias_nombre,
COUNT(nombre)
FROM productos
GROUP BY categorias_nombre;