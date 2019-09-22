import cv2
import numpy as np
x = cv2.__version__
from matplotlib import pyplot as plt


#Función
imagenOriginal = cv2.imread('bandera_original.jpg')
ddepth = -1
np.array([1, 2, 3])
kernel = np.array(( #Los valores del kernel te ayudan a aclarar o volver oscura tu imagen
    #[1, 1, 1],
    #[1, 1, 1],
    #[1, 1, 1]), dtype="int")
	[0, 1, 0],
    [1, 5, 1],
    [0, 1, 0]), dtype="int")

imagenModificada = cv2.filter2D(imagenOriginal, ddepth, kernel)

#imagenModificada =cv2.imwrite('bandera_proceso.jpg',imgTrasformada)

plt.subplot(121),plt.imshow(imagenOriginal),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imagenModificada),plt.title('Convolution')
plt.xticks([]), plt.yticks([])
plt.show()


#cv2.imshow('kernel', img)
#cv2.imwrite('prueba_kernel_otros_numeros.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()