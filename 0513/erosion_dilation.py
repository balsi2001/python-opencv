import cv2
import numpy as np
'''請讀取linuxlogo.jpg檔案, 進行腐蝕與膨脹的練習, 並且與原圖做結果比較。
'''
src = cv2.imread("linuxlogo.jpg")
kernel3 = np.ones((3,3),np.uint8)      
kernel5 = np.ones((5,5),np.uint8)        
dst1 = cv2.erode(src, kernel3)           
      
dst = cv2.dilate(src, kernel5)
cv2.imshow("src",src)
cv2.imshow('after Dilation 5*5',dst)
cv2.imshow("after erosion 3 x 3",dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()
