'''
    Calculadora masas
    Jose Vicente Carratalá
'''
import json

def calcula_masa_atomica(molecula):
    numerodeletras = 0
    for caracter in molecula:
        if caracter.isalpha():
            numerodeletras += 1
    if not "-" in molecula and numerodeletras >= 2:
        return -3
    # Leo el archivo a palo seco
    archivo = open('masas.json','r')
    # Lo convierto en json
    mijson = json.load(archivo)
    #print(mijson)
    # Como parece que va a haber un guion, pues parto
    atomos = molecula.split("-")
    # Vamos a ver los atomos
    #print(atomos)
    # creo una suma de los pesos
    suma = 0
    # Repaso cada atomo
    listaletras = ""
    for atomo in atomos:
        nombredelatomo = ""
        multiplicador = ""
        #print("atomo:",atomo)
        # Y entonces para cada caracter del atomo
        for caracter in atomo:
            #print("caracter:",caracter)
            # Si es alfanumerico, dimelo
            if caracter.isdigit():
                #print("es un caracter numérico")
                multiplicador += caracter
            else:
                #print("es un caracter alfanumerico")
                nombredelatomo += caracter
        # Si la letra ya estaba en la lista de letras, en ese caso devuelve menos 1
        if nombredelatomo in listaletras:
            return -1
        else:
            listaletras += nombredelatomo
        
        if multiplicador == "":
            multiplicador = 1
        #print("El atomo es:",nombredelatomo,"y el multiplicador es",multiplicador)
        if nombredelatomo not in mijson:
            return -2
        peso = mijson[nombredelatomo]
        suma += float(peso)*int(multiplicador)
    suma = round(suma,2)
    return suma

if __name__ == "__main__":
    print(calcula_masa_atomica("N-H3"))
    print(calcula_masa_atomica("C6-H10-O5"))
    print(calcula_masa_atomica("H3-H2"))
    print(calcula_masa_atomica("Tr1-H3"))
    print(calcula_masa_atomica("H2O"))
    print(calcula_masa_atomica("O2"))
