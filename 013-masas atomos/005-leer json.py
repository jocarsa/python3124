'''
    Calculadora masas
    Jose Vicente Carratalá
'''
import json

def calcula_masa_atomica(molecula):
    # Primero lo leo como archivo de texto
    archivo = open("masas.json",'r')
    lineas = archivo.readlines()
    print(lineas)

if __name__ == "__main__":
    print(calcula_masa_atomica("N-H3"))
