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

cursor.execute("SELECT * FROM productos;")
filas = cursor.fetchall()
total = 0
numeroproductos = 0

for fila in filas:
    total += fila[3]
    numeroproductos += 1

promedio = total/numeroproductos
print("El promedio es de:",promedio)

conexion.commit()
