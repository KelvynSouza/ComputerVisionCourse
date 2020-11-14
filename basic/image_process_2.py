import cv2
import numpy as np
from matplotlib import pyplot as plt

def sum_images():
    # Load image
    image = cv2.imread(path_image_1)
    image2 = cv2.imread(path_image_2)
    
    grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grey_image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)    
    show_info(grey_image, True)   
    show_info(grey_image2, True)
    
    image_cropped = grey_image[0:300,0:600]
    image2_cropped = grey_image2[0:300,0:600]
    show_info(image_cropped, True)   
    show_info(image2_cropped, True)
    
    images_sum = image_cropped + image2_cropped;
    show_info(images_sum, True)
    cv2.imshow('image_summed', images_sum)
    
    # the sum will turn the image too bright, because its a sum of the values, so we 
    # average the image
    image_divided = np.divide(image_cropped, 2)
    image2_divided = np.divide(image2_cropped, 2) 
    average = image_divided + image2_divided;
    show_info(average, True)
    
    # A divisão nas imagens transformou eles de uint8 para float64, o matplotlib consegue
    # apresentar a imagem em formato float tranquilamente, porem o imshow do opencv por algum
    # motivo multiplica o valor ao mostrar, tornando tudo branco, por isso a conversão existe
    # apenas após o show_info(). Caso se esqueça disso,tire a conversão e teste ( ;        
    teste = cv2.convertScaleAbs(average)
    cv2.imshow('image_average', teste)
    
    #comparação antes e depois da conversão
    plt.plot(average[50, :])
    plt.plot(teste[50, :])  
    plt.show()            
    
def Scalar():
    # o numero 0.5 pode ser entendido tambem como Scalar, multiplicar uma imagem por ele
    # pode ser entendido como Scalar a imagem 
    image = cv2.imread(path_image_1)
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
       
    image_scalar = image_gray * 0.5
    image_scalar = cv2.convertScaleAbs(image_scalar)
    
    show_info(image_gray,True)
    show_info(image_scalar,True)
    
    cv2.imshow('image_gray', image_gray)
    # O resultado ficara mais obvio aqui
    cv2.imshow('image_scalar 0.5', image_scalar)
    
    # é possivel multiplicar e deixar mais claro tbm
    image_scalar = image_gray * 1.5
    image_scalar = cv2.convertScaleAbs(image_scalar)
    cv2.imshow('image_scalar 1.5', image_scalar)
    

def add_noise():
    #mean of the noise is 0
    image = cv2.imread(path_image_1)   
    
    sigma = 50
    noise = np.random.randn(image.shape[0],image.shape[1],image.shape[2]) * sigma     
    result_image = cv2.convertScaleAbs(image+noise)
    
    cv2.imshow('image_normal', image)
    cv2.imshow('image_noise', result_image)
    

def show_info(image, isgray=False):
    print('-----------------------------------------------------')    
    print('shape:', image.shape, 'and', 'size:', image.size)    
    print(image.dtype)
    
    if isgray:
        plt.imshow(image, cmap='gray')        
    else:
        plt.imshow(image[:,:,::-1])
         
    plt.show()    
    
          
def showable_float_image(image):
    result = cv2.convertScaleAbs(image)
    return result
    
path_image_1 = '../images/In_Game_Image_2.jpg'
path_image_2 = '../images/dolphin.jpg'

add_noise()

cv2.waitKey(0)
cv2.destroyAllWindows()



    
    



