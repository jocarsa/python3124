# pip install mysql-connector-python
# Programa para conectar con bases de datos
import mysql.connector

servidor = "localhost"
usuario = "josevicente"
contrasena = "josevicente"
base_de_datos = "empresa"

connection = mysql.connector.connect(
    host=servidor,      
    database=base_de_datos,  
    user=usuario,  
    password=contrasena  
)
    
if connection.is_connected():
    print("Te has conectado correctamente a la librería")

        
