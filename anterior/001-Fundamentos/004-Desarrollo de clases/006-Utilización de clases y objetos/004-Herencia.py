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

cliente1 = Cliente(1,"Jose Vicente","Carratalá Sanchis","info@josevicente.com","6546546")
cliente2 = Cliente(2,"Juan","García Lopez","juan@josevicente.com","643565464")
print(cliente1.getNombre())
print(cliente2.getNombre())
