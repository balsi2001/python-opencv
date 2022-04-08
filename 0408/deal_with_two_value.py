import cv2 
import numpy as np
import sys
src= cv2.imread(sys.path[0]+'/number1.jpg')
ret,dst=cv2.threshold(src,127,255,cv2.THRESH_BINARY)
cv2.imshow('src',src)
print(ret)
cv2.imshow('dst127',dst)
ret,dst=cv2.threshold(src,0,255,cv2.THRESH_BINARY)
cv2.imshow('dst10',dst)
ret,dst=cv2.threshold(src,0,255,cv2.THRESH_BINARY_INV)
cv2.imshow('dst_inv',dst)
print(ret)
cv2.waitKey(0)
cv2.destroyAllWindows()
