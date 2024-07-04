'''
Programa indexador de discos
v0.1
(c) 2024 Jose Vicente Carratala
'''
#importaciones
import os
import sqlite3


if __name__ == "__main__":
    # Leemos datos de partida
    disco = input("Introduce la unidad de disco a indexar: ")
    contenido = os.walk(disco)
    for root, dirs, files in os.walk(disco):
        print(root,dirs,files)
        print("-----")
