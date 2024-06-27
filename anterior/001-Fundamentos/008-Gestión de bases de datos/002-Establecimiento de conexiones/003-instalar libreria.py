# pip install mysql-connector-python
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',      
    database='empresa',  
    user='josevicente',  
    password='josevicente'  
)
    
if connection.is_connected():
    print("Te has conectado correctamente a la librería")

        
