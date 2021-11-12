import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

sys.path.insert(0, '../util')

from helper import *


def canny_gradient_image():    
    img = cv2.imread(path_image_1)
    img2 = cv2.imread(path_image_2)
    img3 = cv2.imread(path_image_3)
    
    # Estou fazendo o corte pois peguei a imagem do curso por printscreen, 
    # e não ficou igualzinho como deveria
    grey_img = cv2.cvtColor(img[0:img2.shape[0],0:img2.shape[1]], cv2.COLOR_RGB2GRAY)
    grey_img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    grey_img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

    """ 
    https://docs.opencv.org/4.5.3/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de
    Okay, vamos para as explicações, para detecção de bordas existem varios métodos diferentes
    Canny é um dos mais famosos e claro, o que me foi apresentado no curso. Para seu uso 
    existem algumas peculiaridades, primeiro, alem da imagem ele recebe 2 parametros, elas são chamadas de 
    threshold, você coloca o minimo e maximo. O que ele fará, primeiro usará o maior valor
    para capturar as bordas mais fortes e proeminentes, porem isso fará perder muitos detalhes
    dar bordas mais fracas, então usamos o mais fraco e detectamos as bordas fracas que estão 
    de alguma forma entrelaçada com os bordas maiores para pegar o detalhes.
    Detalhes porem ser encontrar em minhas anotações no OneNote
    """
    edg_img = cv2.Canny(grey_img, 30, 60)
    edg_img2 = cv2.Canny(grey_img2, 30, 60)
    edg_img3 = cv2.Canny(grey_img3, 30, 100)

    show_info(edg_img, True)
    show_info(edg_img2, True)
    show_info(edg_img3, True)
    
    #Encontra os pixeis brancos em comum entre as duas imagens, nesse caso, igual ao curso
    #encontrou 007
    result = np.logical_and(edg_img,edg_img2)
    show_info(result, True)

def laplacian_gradient_image(): 
    img = cv2.imread(path_image_3)
    # remove noise
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Reduce noise in image
    img = cv2.GaussianBlur(image_gray,(0,0),2)
    # Filter the image using filter2D, which has inputs: (grayscale image, bit-depth, kernel)
    filtered_image = cv2.Laplacian(img, ksize=3, ddepth=cv2.CV_16S)
    # converting back to uint8
    filtered_image = cv2.convertScaleAbs(filtered_image)
    show_info(filtered_image, True)


path_image_1 = '../../images/frizzy_edge_detection.png'
path_image_2 = '../../images/grummer_edge_detection.png'
path_image_3 = '../../images/miss_edge_detection.png'

laplacian_gradient_image()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



