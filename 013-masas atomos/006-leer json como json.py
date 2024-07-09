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
    print(mijson)

if __name__ == "__main__":
    print(calcula_masa_atomica("N-H3"))
