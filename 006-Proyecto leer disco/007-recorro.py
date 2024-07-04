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
        print(f"Root: {root}")
        print("Directories:")
        for dir_name in dirs:
            print(f"  {dir_name}")
        print("Files:")
        for file_name in files:
            print(f"  {file_name}")
        print("\n")
