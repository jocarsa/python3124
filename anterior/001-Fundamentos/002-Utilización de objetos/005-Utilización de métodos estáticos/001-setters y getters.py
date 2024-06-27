class Persona:
    nombre = None
    apellidos = None
    edad = None
    altura = None

    
    def saluda(self):
        return "Yo me llamo "+self.nombre+" y te saludo"

persona1 = Persona()
persona1.nombre = "Jose Vicente"
print(persona1.nombre)
print(persona1.saluda())

