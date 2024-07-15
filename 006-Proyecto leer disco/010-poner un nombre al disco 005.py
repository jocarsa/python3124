'''
Programa indexador de discos
v0.1
(c) 2024 Jose Vicente Carratala
'''
#importaciones
import os
import sqlite3
import time

def batch_insert(cursor, data_batch):
    cursor.executemany("""
        INSERT INTO archivos
        (disco, carpeta, archivo, modificacion, tamaño, epoch)
        VALUES (?, ?, ?, ?, ?, ?)
    """, data_batch)

if __name__ == "__main__":
    contador = 0
    batch_size = 1000
    data_batch = []

    conexion = sqlite3.connect('discos.db')
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS archivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disco TEXT,
            carpeta TEXT,
            archivo TEXT,
            modificacion REAL,
            tamaño INTEGER,
            epoch REAL
        )
    """)
    
    # Leemos datos de partida
    disco = input("Introduce la unidad de disco a indexar: ")
    
    nombredisco = input("Pon un nombre para identificar a este disco: ")
    print("empezamos")
    contenido = os.walk(disco)
    print("Disco leido, empezamos a procesar")
    
    for root, dirs, files in os.walk(disco):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            try:
                file_size = os.path.getsize(file_path)
            except Exception as e:
                file_size = 0
                
            try:
                modification_time = os.path.getmtime(file_path)
            except Exception as e:
                modification_time = 0
                
            epoch_time = time.time()
            contador += 1

            data_batch.append((nombredisco, root, file_name, modification_time, file_size, epoch_time))

            if contador % batch_size == 0:
                batch_insert(cursor, data_batch)
                conexion.commit()
                data_batch.clear()
                print("#", end=" ")

    if data_batch:
        batch_insert(cursor, data_batch)
        conexion.commit()

    conexion.close()
    print("\nIndexación completa.")
