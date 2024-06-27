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

cursor.execute("DELETE FROM clientes WHERE nombre = 'Jose Vicente';")
conexion.commit()

