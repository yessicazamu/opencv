import cv2
import numpy as np
x = cv2.__version__


np.zeros([520,520,3],np.uint8)
img = np.zeros([520,520,3],np.uint8)

cv2.imshow('arreglo', img)
cv2.imwrite('ejemplo.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()