#pip install pillow
from PIL import Image

imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
print(imagen.size)

        

