agenda = []
agenda.append(
        {
            'nombre':'Jose Vicente',
            'apellidos':'Carratala Sanchis',
            'email':"info@jocarsa.com",
            'telefono':6543645
        }
    )
agenda.append(
        {
            'nombre':'Jaime',
            'apellidos':'Martinez Garcia',
            'email':"jaime@jocarsa.com",
            'telefono':756754675
        }
    )

for registro in agenda:
    print("----------")
    print(registro['nombre'])
    print(registro['apellidos'])
    print(registro['email'])
    print(registro['telefono'])

