from cv2 import *
import shutil
from PIL import Image
from random import randint, uniform,random
import os

##Nombre De la Imagen
file="191002_110516_0000000002_&Cam3Img.jpg"

##Visualizar la Imagen 
img = Image.open(file)
img.show()

##Region (IZQ,ARRIBA,DER,ABAJO)
##Seleccionar la region que se va a cambiar de posicion
region = (2300,5500,2600,5800)
Imagen_Recortada = img.crop(region)
Imagen_Recortada.show()
contador=1
while contador<7:
    ##Region Aleatoria Para que se Inserte la Imagen Modificada
    x1 = randint(300, 3500)
    y1 = randint(400, 16000)
    x2 = x1 + 300
    y2 = y1 + 300

    RegionAleatoria=(x1,y1,x2,y2)


    ##Rotar y pegar la Imagen modificada
    Imagen_Rotada = Imagen_Recortada.transpose(Image.ROTATE_180)
    img.paste(Imagen_Rotada, RegionAleatoria)
    img.save(str(contador)+".jpg")
    shutil.copy(str(contador)+".jpg", 'CarpetaImagenes')
    os.remove(str(contador)+".jpg")
    img.show()
    img= Image.open(file)
    contador=contador+1
    pass



