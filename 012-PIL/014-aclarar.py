#pip install pillow
from PIL import Image

imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
anchura,altura = imagen.size
print(anchura,altura)
pixeles[0,0] = (255,255,255)

for x in range(0,anchura-1):
    for y in range(0,altura-1):
        pixeles[x,y] = (pixeles[x,y][0]+100,pixeles[x,y][1]+100,pixeles[x,y][2]+100)
        

imagen.save("josevicente3.jpg")
