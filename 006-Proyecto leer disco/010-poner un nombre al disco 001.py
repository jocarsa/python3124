'''
Programa indexador de discos
v0.1
(c) 2024 Jose Vicente Carratala
'''
#importaciones
import os
import sqlite3



if __name__ == "__main__":
    conexion = sqlite3.connect('discos.db')
    cursor = conexion.cursor()
    
    # Leemos datos de partida
    disco = input("Introduce la unidad de disco a indexar: ")
    nombredisco = input("Pon un nombre para identificar a este disco: ")
    contenido = os.walk(disco)
    for root, dirs, files in os.walk(disco):
        #print(f"Root: {root}")
        #print("Directories:")
        for dir_name in dirs:
            #print(f"  {dir_name}")
            pass
        #print("Files:")
        for file_name in files:
            file_size = 0
            try:
                file_size = os.path.getsize(root+"/"+file_name)
            except:
                pass
            try:
                modification_time = os.path.getmtime(root+"/"+file_name)
            except:
                pass
            #print(f"  {file_name} - {file_size} - {modification_time}")
            epoch_time = time.time()epoch_time = time.time()
            try:
                cursor.execute(f"""
                INSERT INTO
                archivos
                (nombredisco, root, file_name, modification_time, file_size, epoch_time)
                VALUES (
                '{nombredisco}',
                '{root}',
                '{file_name}',
                '{modification_time}',
                '{file_size}',
                '{epoch_time}')
                """)
                conexion.commit()
                print("#", end=" ")
            except:
                pass
        #print("\n")
    
    conexion.close()
