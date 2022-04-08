import cv2
import numpy as np
src=cv2.imread('forest.jpg')
key=np.random.randint(0,256,src.shape,np.uint8)
img_en=cv2.bitwise_xor(src,key)
img_de=cv2.bitwise_xor(img_en,key)
cv2.imshow("srcimg",src)
cv2.imshow("key",key)
cv2.imshow("encry",img_en)
cv2.imshow("decry",img_de)
cv2.waitKey(0)
cv2.destroyAllWindows()
