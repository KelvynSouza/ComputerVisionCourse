import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

sys.path.insert(0, '../util')

from helper import *

def normalize_image():
    img = cv2.imread(path_image_1)
    show_info(img)

    normalizedImg = np.zeros(img.shape)
    normalizedImg = cv2.normalize(img,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
    show_info(normalizedImg)


def find_in_image(image, template):
    #Esta é a normalização e correlação entre a imagem e o template,
    #Quando a função da o "match" da imagem com o template 
    #Vc vera o lugar com uma Luz branca chamativa na imagem, 
    #este é o local onde ele achou a imagem que ele buscava
    result = normxcorr2(template, image, "same")

    location = np.where(result==result.max())

    y_value = (location[0])[0]
    x_value = (location[1])[0]

    #circulei a luz branca maior que citei mais em cima
    cv2.circle(result, (x_value, y_value), 60, (255, 0, 0), 2)
    show_info(result)

    cv2.circle(image, (x_value, y_value), 60, (255, 0, 0), 2)
    show_info(image)


def better_find_in_image(image, template):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(image, template, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = template.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    # Display the original image with the rectangle around the match.
    show_info(img)


path_image_1 = '../../images/glyph_image.png'

img = cv2.imread(path_image_1)
image_cropped = img[90:200, 180:230]


find_in_image(img, image_cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



