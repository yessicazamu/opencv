import cv2
import numpy as np
x = cv2.__version__
from matplotlib import pyplot as plt


img = cv2.imread('grafica.png',0)
cannyImage = cv2.Canny(img,100,200)  #minimo y maximo de umbral
np.uint8(np.absolute(cannyImage))

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original '), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cannyImage,cmap = 'gray')
plt.title('transformación'), plt.xticks([]), plt.yticks([])
plt.show()