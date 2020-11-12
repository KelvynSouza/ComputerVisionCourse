import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ioff


def process_image(local_image):
    # Load image
    image = cv2.imread(local_image)

    show_info(image)

    grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    show_info(grey_image)

    # Display result image
    cv2.imshow('image_grey', grey_image)
    # cut a image
    image_cropped = grey_image[100:500, 100:500]

    cv2.imshow('image_cropped', image_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_info(image):
    print('-----------------------------------------------------')
    # Get size
    print('shape:', image.shape, 'and ' + 'size:', image.size)
    # get class
    print(image.dtype)
    # value in specific position
    print(image[50, 1])
    # value from all the column
    print(image[50, :])
    # plot information(make a graph with pixels from row)
    plt.plot(image[50, :])
    plt.show()


if __name__ == '__main__':
    path_image = '../images/In_Game_Image_2.jpg'
    process_image(path_image)
