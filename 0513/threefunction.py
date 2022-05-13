'''請讀取lena.jpg影像, 請利用膨脹與腐蝕的函數以及形態學梯度,設計出lena的邊緣影像圖形
'''
import cv2
import numpy as np

src = cv2.imread("lena.jpg")
kernel3 = np.ones((3,3),np.uint8)      
kernel5 = np.ones((5,5),np.uint8)        
dst1 = cv2.erode(src, kernel3)           
morpho=cv2.morphologyEx(src,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))  
dst = cv2.dilate(src, kernel5)
cv2.imshow("src",src)
cv2.imshow('after Dilation 5*5',dst)
cv2.imshow("after erosion 3 x 3",dst1)
cv2.imshow("after morpological 3 x 3",morpho)
cv2.waitKey(0)
cv2.destroyAllWindows()
