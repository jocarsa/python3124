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
    indice = 0
    for linea in contenido:
        # saco el indice de la variable solicitada
        columnas = linea.split(",")
        # Compruebo si la variable está en las columnas
        if variable not in columnas:
            return -1
        # Quiero saber el indice
        indice = columnas.index(variable)
        # Paro la ejecucion del bucle al finalizar la primera iteracion
        break
    # Creo una variable que representa el total de registros
    total = -1
    # Creo una variable que representa los registros que coinciden con lo que busco
    positivos = 0
    # Creo una variable porcentaje que es el resultado final
    porcentaje = 0
    for linea in contenido:
        # El total siempre suma, porque el total es el total de lineas
        total += 1
        # Compruebo si la linea cumple la condicion
        columnas = linea.split(",")
        # Si la columna que busco cumple el requisito solicitado
        if columnas[indice] == str(valor):
            # En ese caso los positivos suman un valor
            positivos += 1
    if positivos == 0:
        return -2
    # pongo el porcentaje
    porcentaje = (positivos/total)*100
    return porcentaje
    
if __name__=="__main__":
    print(enfermedad_cardiovascular('cholesterol',3))
    print(enfermedad_cardiovascular('rh',3))
    print(enfermedad_cardiovascular('cholesterol',5))
