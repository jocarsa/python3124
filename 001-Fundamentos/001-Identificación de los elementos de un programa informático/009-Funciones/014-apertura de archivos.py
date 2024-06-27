# Lector de archivos v 0.1

def get_frec_mutaciones(fich_entrada):
    archivo = open(fich_entrada,'r')
    filas = archivo.readlines()
    for fila in filas:
        print(fila)
    archivo.close()


