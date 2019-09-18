import cv2
import numpy as np
x = cv2.__version__
font = cv2.FONT_HERSHEY_SIMPLEX


def pixelVal(pix, r1, s1, r2, s2):  #transformación del contraste 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 #aumenta la intensidad de una imagen 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 #aumenta la intensidad de una imagen
   
img = cv2.imread('agua.jpg') 
#cv2.putText(img,"disminuye la intensidad de los píxeles oscuros y aumenta la intensidad de los píxeles claros",(100,100), font, 1, (200,0,0), 3, cv2.LINE_AA)
  
#Los valores no pueden valer 0
r1 = 70
s1 = 0
r2 = 140
s2 = 255

pixelVal_vec = np.vectorize(pixelVal) 
  

tranformacion = pixelVal_vec(img, r1, s1, r2, s2) 
   
cv2.imwrite('agua2.jpg', tranformacion) 
cv2.imshow("contraste",tranformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()