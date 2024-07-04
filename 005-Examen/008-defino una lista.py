'''
Programa numero X
por Jose Vicente Carratalá
'''

# Primero importaciones si son necesarias

# Creamos variables globales (intentamos evitarlo)

# Definimos funciones (suele ayudar a realizar cálculos)
def calculaPorcentajesGC(nomfich):
    lista = []
    temporal = None
    archivo = open(nomfich,'r')
    lineas = archivo.readlines()
    for linea in lineas:
        if linea[0] == ">":
            print("Es una cabecera")
            temporal = linea
        else:
            lista.append({temporal:linea})
    print(lista)
    
    
# Creamos método principal
if __name__ == "__main__":
    pass
    # Leemos datos de partida

    # Realizamos operaciones de cálculo
    calculaPorcentajesGC("sampleFasta.fa")
    # Devolvemos resultados
