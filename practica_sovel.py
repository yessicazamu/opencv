import cv2
import numpy as np
x = cv2.__version__
from matplotlib import pyplot as plt

image = cv2.imread('grafica.png')
ddepth = cv2.CV_64F
ksize = 3
x_order = 1
y_order = 0

sovelImagen1 = cv2.Sobel(image,ddepth,1,0,ksize)
sovelImagen2 = cv2.Sobel(image,ddepth,1,0,ksize)
np.uint8(np.absolute(sovelImagen1,sovelImagen2))

resultado=cv2.bitwise_or(sovelImagen1, sovelImagen2)

#mostrando imagen
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(resultado),plt.title('transformación sovel')
plt.xticks([]), plt.yticks([])
plt.show()

