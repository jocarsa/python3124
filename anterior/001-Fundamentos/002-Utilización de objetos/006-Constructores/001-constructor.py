class Persona:
    def __init__(self,minombre,misapellidos,miedad,mialtura):  
        self.nombre = minombre
        self.apellidos = misapellidos
        self.edad = miedad
        self.altura = mialtura
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def getNombre(self):
        return self.nombre
    def saluda(self):
        return "Yo me llamo "+self.nombre+" y te saludo"

persona1 = Persona("Jose Vicente","Carratalá Sanchis",46,1.78)
print(persona1.getNombre())
print(persona1.saluda())

