import pickle
datos = {"cadena": "este es un texto que escribo desde Python"}

with open("fichero.bin", 'wb') as archivo:
    pickle.dump(datos, archivo)

archivo_size = len(pickle.dumps(datos))

