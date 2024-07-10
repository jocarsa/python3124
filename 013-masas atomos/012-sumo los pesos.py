'''
    Calculadora masas
    Jose Vicente Carratalá
'''
import json

def calcula_masa_atomica(molecula):
    # Leo el archivo a palo seco
    archivo = open('masas.json','r')
    # Lo convierto en json
    mijson = json.load(archivo)
    #print(mijson)
    # Como parece que va a haber un guion, pues parto
    atomos = molecula.split("-")
    # Vamos a ver los atomos
    print(atomos)
    # creo una suma de los pesos
    suma = 0
    # Repaso cada atomo
    for atomo in atomos:
        nombredelatomo = ""
        multiplicador = ""
        print("atomo:",atomo)
        # Y entonces para cada caracter del atomo
        for caracter in atomo:
            print("caracter:",caracter)
            # Si es alfanumerico, dimelo
            if caracter.isdigit():
                print("es un caracter numérico")
                multiplicador += caracter
            else:
                print("es un caracter alfanumerico")
                nombredelatomo += caracter
        if multiplicador == "":
            multiplicador = 1
        print("El atomo es:",nombredelatomo,"y el multiplicador es",multiplicador)
        peso = mijson[nombredelatomo]
        suma += float(peso)*int(multiplicador)
    return suma

if __name__ == "__main__":
    print(calcula_masa_atomica("N-H3"))
