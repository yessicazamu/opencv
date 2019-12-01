import cv2
x = cv2.__version__

img_gris = cv2.imread('imagen.jpg',0)
cv2.imwrite('nueva_gris.jpg',img_gris) #escala de gris el valor, 0
cv2.imshow('window image', img_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

