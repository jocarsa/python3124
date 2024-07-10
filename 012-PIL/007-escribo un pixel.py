#pip install pillow
from PIL import Image

imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
print(pixeles[0,0])
blanco = (255,255,255)
pixeles[0,0] = blanco

