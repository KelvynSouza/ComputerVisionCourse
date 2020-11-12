import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ioff

def sum_images():
    # Load image
    image = cv2.imread(path_image_1)
    image2 = cv2.imread(path_image_2)
    
    show_info(image)   
    show_info(image2) 
    
    image_result = image[0:300,0:600] + image2[0:300,0:600]
    
    #the sum will turn the image too bright, because its a sum of the values, so we average the image
    average = image[0:300,0:600] / 2 + image2[0:300,0:600] / 2
    
    show_info(image_result, True)
    show_info(average,True)

def show_info(image, isgray=False):
    print('-----------------------------------------------------')
    # Get size
    print('shape:', image.shape, 'and ' + 'size:', image.size)
    # get class
    print(image.dtype)
    # plot information(make a graph with pixels from row)
    if isgray:
        plt.imshow(image, cmap='gray')        
    else:
        plt.imshow(image[:,:,::-1])
         
    plt.show()
    

path_image_1 = '../images/In_Game_Image_2.jpg'
path_image_2 = '../images/dolphin.jpg'

sum_images()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



