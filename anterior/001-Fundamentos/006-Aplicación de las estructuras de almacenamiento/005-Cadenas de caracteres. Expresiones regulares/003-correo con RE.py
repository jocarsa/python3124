import re
patron = r"^\S+@\S+\.\S+$"
email = "info@josevicentecarratala.com"

resultado = re.match(patron,email)
if resultado != None:
    print("es un correo")
else:
    print("no es un correo")
