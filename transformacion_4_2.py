import cv2
import numpy as np
x = cv2.__version__
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread('flores.jpg')
cv2.putText(img,"aumenta en 2.2 la intensidad del color de la imagen",(100,100), font, 1, (8,8,7), 3, cv2.LINE_AA)
gamma = 2.2

transformacion = np.array(255*(img / 255) ** gamma, dtype ='uint8') #Aumenta el color de la imagen segun el gamma

cv2.imwrite('flores2.jpg',transformacion)
cv2.imshow("transformacion",transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()
