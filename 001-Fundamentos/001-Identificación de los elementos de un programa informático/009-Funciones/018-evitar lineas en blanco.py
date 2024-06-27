# Lector de archivos v 0.1

def get_frec_mutaciones(fich_entrada):
    archivo = open(fich_entrada,'r')
    filas = archivo.readlines()
    diccionario = {}
    for fila in filas:
        if fila != "\n":
            clave = fila.split(",")[0]
            valor = fila.split(",")[1]
            diccionario[clave] = valor
    archivo.close()
    return diccionario

print(get_frec_mutaciones("datos2.txt"))
