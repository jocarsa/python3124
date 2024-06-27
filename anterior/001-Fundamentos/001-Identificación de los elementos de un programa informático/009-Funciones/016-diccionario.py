# Lector de archivos v 0.1

def get_frec_mutaciones(fich_entrada):
    archivo = open(fich_entrada,'r')
    filas = archivo.readlines()
    diccionario = {}
    for fila in filas:
        clave = fila.split(",")[0]
        valor = fila.split(",")[1]
        diccionario[clave] = valor
    print(diccionario)
    archivo.close()

get_frec_mutaciones("datos.txt")
