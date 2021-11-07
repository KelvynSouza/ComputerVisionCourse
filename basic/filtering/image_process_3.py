import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

sys.path.insert(0, '../util')

from helper import show_info

def noise_sample():
    #mean of the noise is 0
    image = cv2.imread(path_image_1) 

    grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_info(grey_image, True)

    noisy_image = add_saltpepper_noise(grey_image)
    show_info(noisy_image, True) 

    filtered__image = cv2.medianBlur(noisy_image, 3) 
    show_info(filtered__image, True) 
    
def add_saltpepper_noise(image):
    row,col = image.shape
    s_vs_p = 0.5
    amount = 0.04
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[tuple(coords)] = 255
    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[tuple(coords)] = 0
    return out

path_image_1 = '../../images/moon_image.png'

noise_sample()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



