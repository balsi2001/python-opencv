import cv2
import numpy as np

'''
請建立一個400X400的畫布, 在畫布內建立半徑140的實心白色圓形, 並輸出下列影像:

1.原始影像

2.沒有做絕對值處理的X軸影像梯度

3.有做絕對值處理的X軸影像梯度

4.有做絕對值處理的Y軸影像梯度

5.將二個梯度整合成一個完整的梯度, 並列出影像邊緣
'''
src=np.zeros((400,400),np.uint8)
cv2.circle(src, (int(src.shape[0]/2), int(src.shape[1]/2)), 140, (255, 255, 255), -1)
cv2.imshow('src',src)
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
cv2.imshow('dstx_8u',dstx)  
dstx = cv2.convertScaleAbs(dstx)  
cv2.imshow('dstx',dstx)  
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)
cv2.imshow('dsty_8u',dsty) 
dsty = cv2.convertScaleAbs(dsty)
'''cv2.CV_8U

'''
cv2.imshow('dsty',dsty) 
dst_merge =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)
cv2.imshow('dst',dst_merge) 
cv2.waitKey(0)

