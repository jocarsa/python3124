# Programa de gestión empresarial
# v0.1 por Jose Vicente Carratalá

class Cliente:
    def __init__(self,miid,minombre,misapellidos,miemail,mitelefono):
        self.identificador = miid
        self.nombre = minombre
        self.apellidos = misapellidos
        self.email = miemail
        self.telefono = mitelefono
    def setNombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
    def getNombre(self):
        return self.nombre
    def setApellidos(self,nuevos_apellidos):
        self.nombre = nuevos_apellidos
    def getApellidos(self):
        return self.nombre
    def setEmail(self,nuevo_email):
        self.nombre = nuevo_email
    def getEmail(self):
        return self.nombre
    def setTelefono(self,nuevo_telefono):
        self.nombre = nuevo_telefono
    def getTelefono(self):
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
    nombre = input("Introduce un nuevo nombre:")
    apellidos = input("Introduce los apellidos:")
    email = input("Introduce el email:")
    telefono = input("Introduce el telefono:")
    agenda = Cliente(1,nombre,apellidos,email,telefono)
elif opcion == 3:
    print("Actualizamos un registro")
elif opcion == 4:
    print("Eliminamos un registro")

print(agenda)
