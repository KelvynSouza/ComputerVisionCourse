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


def find_in_image():
    img = cv2.imread(path_image_1)
    show_info(img)

    image_cropped = img[90:200, 180:230]
    show_info(image_cropped)

    result = normxcorr2(image_cropped, img, "same")
    show_info(result)

    location = np.nonzero(result==result.max())

    print(location)


path_image_1 = '../../images/glyph_image.png'

find_in_image()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



