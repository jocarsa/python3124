import mysql.connector

servidor = "localhost"
usuario = "josevicente"
contrasena = "josevicente"
base_de_datos = "empresa"

conexion = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)

cursor = conexion.cursor()

cursor.execute("SELECT AVG(precio) AS promedio FROM productos;")
filas = cursor.fetchall()

for fila in filas:
    print("el promedio es",fila[0])

conexion.commit()
