import cv2
x = cv2.__version__

img = cv2.imread('yessi.jpg',-5)
cv2.imshow('window image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_gris = cv2.imread('yessi.jpg',60)
cv2.imwrite('funciona.jpg',img_gris) #escala de gris el valor, 0

img_rgb = cv2.imread('yessi.jpg',20)
cv2.imwrite('yessi2.jpg',img_rgb) #escala de rgb el valor, 20

img_alpha = cv2.imread('yessi.jpg',-5)
cv2.imwrite('yessi3.jpg',img_alpha) #escala de alpha el valor, -10
