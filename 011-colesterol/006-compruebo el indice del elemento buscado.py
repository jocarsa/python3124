'''
    Ejercicio residuos
    Jose Vicente Carratalá
'''

def enfermedad_cardiovascular(variable,valor):
    # Primero leo los datos
    archivo = open('cardio.csv','r')
    # Ahora leo todo
    contenido = archivo.readlines()
    # Ahora leo linea a linea
    for linea in contenido:
        # saco el indice de la variable solicitada
        columnas = linea.split(",")
        # Imprimo lo que tengo hasta el momento
        print(columnas)
        # Quiero saber el indice
        indice = columnas.index(variable)
        # Imprimo lo que tengo hasta el momento
        print("El indice es:",indice)
        # Paro la ejecucion del bucle al finalizar la primera iteracion
        break

if __name__=="__main__":
    print(enfermedad_cardiovascular('cholesterol',3))
