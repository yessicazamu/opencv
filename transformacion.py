import cv2
import numpy as np
x = cv2.__version__
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread('arbol.jpg')

cv2.putText(img,"255 maximo de color dividido entre el algoritmo natural del maximo de la imagen",(100,100), font, 1, (200,0,0), 3, cv2.LINE_AA)
c = 255/(np.log(1 + np.max(img))) #obtenemos el algoritmo natural del arreglo sobre el maximo de color que es el 255

transformacion = c * np.log1p(img) #le coloca iluminación a la imagen 

transformacion = np.array(transformacion, dtype = np.uint8)


cv2.imwrite('arbol2.jpg',transformacion)
cv2.imshow("tranformando",transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()