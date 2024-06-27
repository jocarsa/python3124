class Persona:
    nombre = None
    apellidos = None
    edad = None
    altura = None

    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def getNombre(self):
        return self.nombre
    def saluda(self):
        return "Yo me llamo "+self.nombre+" y te saludo"

persona1 = Persona()
persona1.setNombre("Jose Vicente")
print(persona1.getNombre())
print(persona1.saluda())

