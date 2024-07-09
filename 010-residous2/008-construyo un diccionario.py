'''
    Ejercicio residuos
    Jose Vicente Carratalá
'''

molecula="""
ATOM 1 N         HIS A 1 49.668 24.248 10.436 1.00 25.00 N
ATOM 2 CA        HIS A 1 50.197 25.578 10.784 1.00 16.00 C
ATOM 3 C         HIS A 1 49.169 26.701 10.917 1.00 16.00 C
ATOM 4 O         HIS A 1 48.241 26.524 11.749 1.00 16.00 O
ATOM 5 CB        HIS A 1 51.312 26.048 9.843 1.00 16.00 C
ATOM 6 CG        HIS A 1 50.958 26.068 8.340 1.00 16.00 C
ATOM 7 ND1       HIS A 1 49.636 26.144 7.860 1.00 16.00 N
ATOM 8 CD2       HIS A 1 51.797 26.043 7.286 1.00 16.00 C
ATOM 9 CE1       HIS A 1 49.691 26.152 6.454 1.00 17.00 C
ATOM 10 NE2      HIS A 1 51.046 26.090 6.098 1.00 17.00 N
ATOM 11 N        SER A 2 49.788 27.850 10.784 1.00 16.00 N
ATOM 12 CA       SER A 2 49.138 29.147 10.620 1.00 15.00 C
ATOM 13 C        SER A 2 47.713 29.006 10.110 1.00 15.00 C
ATOM 14 O        SER A 2 46.740 29.251 10.864 1.00 15.00 O
ATOM 15 CB       SER A 2 49.875 29.930 9.569 1.00 16.00 C
ATOM 16 OG       SER A 2 49.145 31.057 9.176 1.00 19.00 O
ATOM 17 N        GLN A 3 47.620 28.367 8.973 1.00 15.00 N
ATOM 18 CA       GLN A 3 46.287 28.193 8.308 1.00 14.00 C
ATOM 19 C        GLN A 3 45.406 27.172 8.963 1.00 14.00 C
"""

def dameResiduos(molecula):
    # Tomo la cadena y la divido en diferentes lineas
    lineas = molecula.split("\n")
    # Saco por pantalla lo que he hecho hasta este momento
    print(lineas)
    # Creo una nueva lista vacía
    atomos = []
    # Para cada una de las lineas en la estructura
    for linea in lineas:
        # Si la linea está vacía
        if linea == '':
            pass # En ese caso no hagas nada
        else: # Pero si la linea no está vacía
            # En ese caso añádela a la estructura de átomos
            atomos.append(linea)
    # Saco por pantalla lo que he hecho hasta este momento
    print(atomos)
    # creo un diccionario vacío
    diccionario = {}
    # Repaso la lista limpiada
    for atomo in atomos:
        # Imprimeme solo el caracter 18
        # Sería el índice 18 pero le resto un valor porque las listas empiezan en cero y no en uno
        residuo = atomo[18-1]+atomo[19-1]+atomo[20-1]
        # Saco por pantalla lo que he hecho hasta este momento
        print(residuo)
        # Si el residuo está en el diccionario
        if residuo in diccionario:
            # Entonces suma un valor a lo que ya valía
            diccionario[residuo] += 1
        else: # en caso contrario eso quiere decir que no existía
            # Entonces lo añado al diccionario y lo inicializo a 1
            diccionario[residuo] = 1
        # Saco por pantalla lo que he hecho hasta este momento
        print(diccionario)

if __name__=="__main__":
    print(dameResiduos(molecula)) #{'HIS': 10, 'SER': 6, 'GLN': 3}






    
