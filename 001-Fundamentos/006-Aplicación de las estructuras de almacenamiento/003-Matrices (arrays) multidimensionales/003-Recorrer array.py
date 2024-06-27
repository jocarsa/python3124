agenda = []
agenda.append(['Jose Vicente','Carratala Sanchis',"info@jocarsa.com",6543645])
agenda.append(['Juan','García Lopez',"juan@jocarsa.com",6543645])
for registro in agenda:
    print("----------------")
    print("Nombre: "+registro[0])
    print("Apellidos: "+registro[1])
    print("Correo: "+registro[2])
    print("Telefono: "+str(registro[3]))
