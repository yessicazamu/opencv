import cv2
import numpy as np
x = cv2.__version__

imagenFuente = cv2.imread('laparka.jpeg')
ddepth = -1
np.array([1, 2, 3])
kernel = np.array(( #Los valores del kernel te ayudan a aclarar o volver oscura tu imagen
    #[1, 1, 1],
    #[1, 1, 1],
    #[1, 1, 1]), dtype="int")
	[0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

imgTrasformada = cv2.filter2D(imagenFuente, ddepth, kernel)
cv2.imshow('kernel', imgTrasformada)
cv2.imwrite('prueba_kernel_otros_numeros.png',imgTrasformada)
cv2.waitKey(0)
cv2.destroyAllWindows()