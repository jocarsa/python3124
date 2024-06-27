print("Indica tu acción:")
print("1.-Listar nombres")
print("2.-Introducir un nuevo nombre")
opcion = input("Escoge una opcion: ")
opcion = int(opcion)
if opcion == 1:
    archivo = open("nombres.txt",'r')
    contenido = archivo.readlines()
    for linea in contenido:
        print(linea)
elif opcion == 2:
    nombre = input("Introduce un nuevo nombre: ")
    archivo = open("nombres.txt",'a')
    archivo.write(nombre+"\n")
    archivo.close()
