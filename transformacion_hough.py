import cv2
import numpy as np
x = cv2.__version__
from matplotlib import pyplot as plt

original = cv2.imread('sudoku.png')
img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200) #linea vertical y si es 180 sera una linea horizontal
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b)) #asignamos la posición en donde se colocara la imagen
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    imgTransformada = cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#cv2.imwrite('houghlines1.jpg',img)
plt.subplot(121),plt.imshow(original),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgTransformada),plt.title('transformación Hough')
plt.xticks([]), plt.yticks([])
plt.show()
