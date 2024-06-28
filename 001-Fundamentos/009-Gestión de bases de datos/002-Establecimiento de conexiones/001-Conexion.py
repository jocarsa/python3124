
connection = mysql.connector.connect(
    host='localhost',      
    database='empresa',  
    user='josevicente',  
    password='josevicente'  
)
    
if connection.is_connected():
    print("Successfully connected to the database")

        
