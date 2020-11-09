import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import ioff


def process_image(local_image):

    # Load image
    image = cv2.imread(local_image)
    show_info(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_info(image)

    # Display result image
    cv2.imshow('image', image)

    # cut a image
    image_cropped = image[100:500, 100:500]
    cv2.imshow('image 2', image_cropped)

    cv2.waitKey(0)


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

