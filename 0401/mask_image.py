import cv2
import numpy as np
src=cv2.imread('geneva.jpg')

cv2.imshow('geneva',src)
mask=np.zeros(src.shape,dtype=np.uint8)
print(src.shape)
x=0
y=0
mask[0:303,144:288,:]=255
mask[101:202,0:433,:]=255
cv2.imshow('mask',mask)
res=cv2.bitwise_or(src,mask)
res2=cv2.bitwise_and(src,mask)
cv2.imshow('r',res)
cv2.imshow('r1',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()


