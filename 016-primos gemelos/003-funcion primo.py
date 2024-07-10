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

if __name__ == "__main__":
    print(esPrimo(4))
    print(esPrimo(5))
