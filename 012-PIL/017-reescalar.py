#pip install pillow
from PIL import Image

imagen = Image.open("josevicente.jpg")
imagen = imagen.resize((40,60))
pixeles = imagen.load()
anchura,altura = imagen.size
print(anchura,altura)
pixeles[0,0] = (255,255,255)

for x in range(0,anchura-1):
    for y in range(0,altura-1):
        promedio = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
        pixeles[x,y] = (promedio,promedio,promedio)
        
imagen.save("josevicente3.jpg")
