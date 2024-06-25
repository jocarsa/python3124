# Programa de gestión empresarial
# v0.1 por Jose Vicente Carratalá

class Persona:
    def __init__(self,minombre,misapellidos,miemail,mitelefono):  
        self.nombre = minombre
        self.apellidos = misapellidos
        self.email = miemail
        self.telefono = mitelefono
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def getNombre(self):
        return self.nombre

TITULO_DEL_PROGRAMA = "Programa de gestión"
VERSION = "v0.1"
ANIO = 2024
AUTOR = "Jose Vicente Carratalá"

print(f"{TITULO_DEL_PROGRAMA} {VERSION}")
print(f"(c) {ANIO} {AUTOR}")
print("Escoge una opción:")
print("1.-Listar registros")
print("2.-Insertar un registro")
print("3.-Actualizar un registro")
print("4.-Eliminar un registro")
opcion = input("Tu opción: ")
opcion = int(opcion)
if opcion == 1:
    print("Listado de registros")
elif opcion == 2:
    print("Insertamos un nuevo registro")
elif opcion == 3:
    print("Actualizamos un registro")
elif opcion == 4:
    print("Eliminamos un registro")
