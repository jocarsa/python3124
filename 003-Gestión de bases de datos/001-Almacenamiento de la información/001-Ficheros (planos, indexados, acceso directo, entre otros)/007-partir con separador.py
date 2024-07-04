archivo = open("fichero.txt",'r')
contenido = archivo.readline()
palabras = contenido.split(" ")
print(palabras)
