import cv2
import numpy as np
x = cv2.__version__
font = cv2.FONT_HERSHEY_SIMPLEX

def negative(l):
    #Cargar imagen
    img = cv2.imread("paisaje.jpg", cv2.IMREAD_GRAYSCALE)
    rows, columns = img.shape
    img2 = np.zeros((rows, columns), dtype = np.uint8)
    for x in range(rows):
        for y in range(columns):
            img2[x, y] = (l-1)-img[x,y]

    cv2.imwrite("paisaje2.jpg",img2)
    cv2.imshow('negativo',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

