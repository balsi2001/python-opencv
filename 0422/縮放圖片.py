import cv2
from cv2 import RNG_NORMAL
import  numpy as np
src=cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('',src)

small=np.zeros((int(src.shape[0]/2),int(src.shape[1]/2)),np.uint8)

print(len(src[0]))

print(len(src[1]))
for i in range(0,316):
    for j in range(0,316):
        small[int(i/2),int(j/2)]=src[i,j]
big=np.zeros((158*2,158*2),np.uint8)
for i in range(0,316):
    for j in range(0,316):
        big[i,j]=small[int(i/2),int(j/2)]

cv2.imshow('s',small)
cv2.imshow('b',big)
cv2.waitKey(0)
cv2.destroyAllWindows()
