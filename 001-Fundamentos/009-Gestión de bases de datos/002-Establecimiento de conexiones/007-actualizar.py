# pip install mysql-connector-python
# Programa para conectar con bases de datos
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

cursor.execute("UPDATE clientes SET telefono = '12345678' WHERE nombre = 'Jose Vicente';")
conexion.commit()

cursor.execute("SELECT * FROM clientes;")
filas = cursor.fetchall()

for fila in filas:
    print(f'{fila[0]} - {fila[1]} - {fila[2]} - {fila[3]}')

conexion.commit()
