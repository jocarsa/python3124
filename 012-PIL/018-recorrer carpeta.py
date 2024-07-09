#pip install pillow
from PIL import Image, ExifTags
import os

carpeta = "seleccion"
archivos = os.listdir(carpeta)

for archivo in archivos:
    imagen = Image.open(carpeta+"/"+archivo)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = imagen._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                imagen = imagen.rotate(180, expand=True)
            elif orientation_value == 6:
                imagen = imagen.rotate(270, expand=True)
            elif orientation_value == 8:
                imagen = imagen.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass
    imagen = imagen.resize((40,60))
    pixeles = imagen.load()
    anchura,altura = imagen.size
    print(anchura,altura)
    pixeles[0,0] = (255,255,255)

    for x in range(0,anchura-1):
        for y in range(0,altura-1):
            promedio = round((pixeles[x,y][0]+pixeles[x,y][1]+pixeles[x,y][2])/3)
            pixeles[x,y] = (promedio,promedio,promedio)
            
    imagen.save(carpeta+"/_"+archivo)
