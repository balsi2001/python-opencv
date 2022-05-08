import cv2
import numpy as np
src = cv2.imread('Baboon256.bmp',0)

'''
請讀取Baboon256圖檔, 分別使用Sobel, Canny（低閾值50, 高閾值=80), 以Laplacian(Ksize=3)及Scharr四個函數的來建立影像的邊緣。
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

cv2.imshow("Src", src)       
cv2.imshow("Sobel", dst_sobel)
cv2.imshow('Scharr', dst_scharr) 
cv2.imshow("Laplacian", dst_lap)      
src=cv2.GaussianBlur(src,(3,3),2)
ocan=cv2.Canny(src, 50, 80)
cv2.imshow('canny',ocan)
cv2.waitKey(0)      
cv2.destroyAllWindows() 
