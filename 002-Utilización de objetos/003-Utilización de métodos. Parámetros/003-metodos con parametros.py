class Persona:
    nombre = "Jose Vicente"
    apellidos = "Carratalá Sanchis"
    edad = 46
    altura = 1.78

    def saluda(self):
        return "Yo me llamo "+self.nombre+" y te saludo"

persona1 = Persona()
print(persona1.nombre)
print(persona1.saluda())

