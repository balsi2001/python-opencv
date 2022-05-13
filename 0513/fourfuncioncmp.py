import cv2
import numpy as np
src = cv2.imread('lena.jpg')

'''
請使用snowman.jpg, 列出此影像的邊緣並與上禮拜的Sobel、Scharr、Laplacian函數所做出的影像邊緣做比較。
'''
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst_sobel =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)    # 影像融合
# Scharr()函數
dstx = cv2.Scharr(src, cv2.CV_32F, 1, 0)        # 計算 x 軸影像梯度
dsty = cv2.Scharr(src, cv2.CV_32F, 0, 1)        # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst_scharr =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)   # 影像融合
# 輸出影像梯度
dstmp=cv2.Laplacian(src,cv2.CV_32F,ksize=3)
dst_lap=cv2.convertScaleAbs(dstmp)
morpho=cv2.morphologyEx(src,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))  
cv2.imshow("Src", src)       
cv2.imshow("Sobel", dst_sobel)
cv2.imshow('Scharr', dst_scharr) 
cv2.imshow("Laplacian", dst_lap)      
cv2.imshow("after morpological 3 x 3",morpho)
cv2.waitKey(0)      
cv2.destroyAllWindows() 