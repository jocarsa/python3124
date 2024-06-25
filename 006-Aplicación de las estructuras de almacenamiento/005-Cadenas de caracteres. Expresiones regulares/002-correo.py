email = "info@josevicentecarratala"

resultado = False
for letra in email:
    if letra == "@":
        resultado = True

if resultado == True:
    print("es un correo")
