'''
    Primos gemelos
    Jose Vicente Carratalá
'''

def esPrimo(n):
    if n <= 3:
        return (n > 1)
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i=5
    while(i*i <= n):
        if (n%i == 0) or (n%(i+2) == 0):
            return False
        i=i+6
    return True

def dameParejasPrimosGemelos(lista):
    inicio = lista[0]
    final = lista[1]
    if inicio[1] == True:
        numinicio = inicio[0]
    else:
        numinicio = inicio[0]+1
    if final[1] == True:
        numfinal = final[0]
    else:
        numfinal = final[0]-1
    print(numinicio,numfinal)
    for numero in range(numinicio,numfinal+1):
        print(numero)

if __name__ == "__main__":
    print(dameParejasPrimosGemelos([(10,True),(150,False)]))
