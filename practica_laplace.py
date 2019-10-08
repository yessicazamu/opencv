import cv2
import numpy as np
x = cv2.__version__
from matplotlib import pyplot as plt

image = cv2.imread('grafica.png')
ddepth = cv2.CV_64F
ksize = 3
laplaceImage = cv2.Laplacian(image,ddepth,ksize)

np.uint8(np.absolute(laplaceImage))

titles = ['original', 'Laplacian']
images = [image, laplaceImage]

for i in range(2):
	plt.subplot(1,2,i+1) #row, column, ...
	plt.imshow(images[i], 'gray') #imagenes a mostrar
	plt.title(titles[i]) #titulos de las imagenes
	plt.xticks([]), plt.yticks([])
plt.show()