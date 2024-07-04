'''
Programa numero X
por Jose Vicente Carratalá
'''

# Primero importaciones si son necesarias

# Creamos variables globales (intentamos evitarlo)

# Definimos funciones (suele ayudar a realizar cálculos)
def calculaPorcentajesGC(nomfich):
    # Leemos datos de partida
    lista = []
    resultados = []
    temporal = None
    archivo = open(nomfich,'r')
    salida = open("salida.gc","a")
    lineas = archivo.readlines()
    for linea in lineas:
        if linea[0] == ">":
            temporal = linea.replace(">","").replace("\n","")
        else:
            lista.append({"persona":temporal,"nucleotidos":linea.replace("\n","")})
    # ahora leo la lista elemento a elemento
    for elemento in lista:
        cadena = elemento['nucleotidos']
        contador = 0
        for nucleotido in cadena:
            if nucleotido == "G" or nucleotido == "C":
                contador += 1
        total = (contador/len(cadena))*100
        resultados.append(total)
        salida.write(">"+elemento['persona']+":"+str(round(total,2))+"\n")
    # Devolvemos resultados
    return resultados
    
    
# Creamos método principal
if __name__ == "__main__":
    # Realizamos operaciones de cálculo
    print(calculaPorcentajesGC("sampleFasta.fa"))
    
