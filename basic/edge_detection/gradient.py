import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

sys.path.insert(0, '../util')

from helper import *

# https://docs.opencv.org/4.5.3/d5/d0f/tutorial_py_gradients.html
# Existem diversas funções para obter a imagem gradiente
# aqui estamos usando a Sobel, gradientes são um passo em 
# busca da detecção de bordas "edges", é possivel fazer a função 
# na direção x e y, mudando os parametro no Sobel()
def gradient_image():
    img = cv2.imread(path_image_1)
    #convert image to float for better precision
    img = img / 255. 
    show_info(img)

    # Criar gradiente com metodo de Sobel em direção x
    sobel_x = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)   
    
    # Criar gradiente com metodo de Sobel em direção y
    sobel_y = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)     

    # obter magnitude do gradiente, usando os 2 criados anteriormente
    magnitude = np.sqrt(sobel_x**2.0 + sobel_y**2.0)
    # obter o angulo do gradiente, a direção é apontada por angulo mesmo
    # por exemplo 360º
    angle = np.arctan2(sobel_y, sobel_x) * (180 / np.pi)

    #Normalizar e mostrar a magnitute dos gradientes
    result_magnitude = magnitude / (4*np.sqrt(2))
    show_info(result_magnitude)

    result_angle = ((angle+180.0)/360.0)
    show_info(result_angle)


def better_gradient_image():    
    img = cv2.imread(path_image_1)

    # Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U    
    sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
    abs_sobel64f = np.absolute(sobelx64f)
    sobel_8u = np.uint8(abs_sobel64f)

    show_info(sobel_8u)

path_image_1 = '../../images/gradiant_octagon.png'

better_gradient_image()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



