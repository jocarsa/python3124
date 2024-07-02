class Programa():
    def __init__(self):
        pass       
    def inicio(self):
        print("Ejecuto el programa")
    def suma(self):
        return(2+2)
        
if __name__ == "__main__":
    programa = Programa()
    programa.inicio()
    print(programa.suma())
