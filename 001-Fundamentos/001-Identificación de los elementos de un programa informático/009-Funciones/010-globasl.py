nombre_programa = "Programa funciones"

def emiteSaludo(nombre,edad):
    global nombre_programa
    nombre_programa = "Otro nombre"
    return f'''
    Hola, este es el programa llamado {nombre_programa}
    y me llamo {nombre}
    y tengo {edad} años
    '''


print(emiteSaludo("Jose Vicente",46))
print(emiteSaludo("Juan",47))
    
print("El nombre del programa es:",nombre_programa)
