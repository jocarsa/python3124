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
    # Repaso cada atomo
    for atomo in atomos:
        print("atomo:",atomo)
        # Y entonces para cada caracter del atomo
        for caracter in atomo:
            print("caracter:",caracter)
            # Si es alfanumerico, dimelo
            if caracter.isalpha():
                print("es un caracter alfanumerico")
            # Si es numérico, dímelo
            if caracter.isdigit():
                print("es un caracter numérico")

if __name__ == "__main__":
    print(calcula_masa_atomica("N-H3"))
