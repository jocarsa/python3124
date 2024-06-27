nombre = input("Introduce un nuevo nombre: ")

print("Indica tu acción:")
print("1.-Listar nombres")
print("2.-Introducir un nuevo nombre")
opcion = input("Escoge una opcion: ")
opcion = int(opcion)

archivo = open("nombres.txt",'a')
archivo.write(nombre+"\n")
archivo.close()
