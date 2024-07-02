def dHamming(cadena1,cadena2):
    distancia = 0
    for i in range(0,len(cadena1)):
        if cadena1[i] != cadena2[i]:
            distancia += 1
    return distancia

if __name__ == "__main__":
    p = 'CCGAAGCAATTGAAACCCCCCCGGCCTGGGAGGCGCAAAAATCTGACCTCTTTGTGAGT'
    q = 'GCGTAGTAGGTTCGCGTACCTCGTTCCGGGGAAAACACAAAGGAGAAGGGAATGCTCCT'
    print(dHamming(p,q)) #35
