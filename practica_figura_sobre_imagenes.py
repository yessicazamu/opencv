import cv2
x = cv2.__version__

img = cv2.imread('Lienzo-blanco1.jpg')
#cv2.imshow('window image', img)



cv2.arrowedLine(img, (40,50), (800,50), (50,168,155), 15) #coordenada inicio, coordenada final, color de la linea, grosor
cv2.line(img, (20,500), (800,500), (168,162,50), 5)
cv2.rectangle(img, (20,80), (300+30,300+30), (23,22,22), 10)
cv2.circle(img, (600,200), 50, (31,23,99), 3)

cv2.imwrite('Lienzo-blanco.jpg',img)

cv2.imshow("Paint",img)
cv2.waitKey(0)
cv2.destroyAllWindows()