nombre = input("Introduce un nuevo nombre: ")

archivo = open("nombres.txt",'a')
archivo.write(nombre+"\n")
archivo.close()
