class Persona:
    nombre = "Jose Vicente"
    apellidos = "Carratalá Sanchis"
    edad = 46
    altura = 1.78

    def saluda(self):
        print("Yo te saludo")

persona1 = Persona()
print(persona1.nombre)
persona1.saluda()

