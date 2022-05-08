
import cv2
import numpy as np
src = cv2.imread('lena.jpg',0)

cv2.imshow("Src", src)

org=np.zeros((int(src.shape[0]),int(src.shape[1])),np.uint8)
orh=src
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)  # 影像融合
cv2.imshow("Dst", dst)
gx=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
#gx=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
#gx=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
gx=np.array(gx)
gy=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
#gy=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
#gy=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
gy=np.array(gy)

gg=np.array([[0,0],[1,1],[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]])

for i in range(1,323):
    t=0
    x=0
    y=0
    for j in range(1,320):
        x=0
        y=0
        for k,l in gg:
            x+=(src[i+k,j+l]*gx[1+k,1+l])
            y+=(src[i+k,j+l]*gy[1+k,1+l])
        t=(((x)**2)+((y)**2))**0.5
        org[i,j]=t

cv2.imshow('org',org)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
i-1=0
i+1=2
j-1=0
j+1=2
i=1 ,j=1
00 01 02   00 01 02  -1  0 1 | -1 -2 -1
10 11 12 * 10 11 12  -2  0 2 | 0  0  0
20 21 22   20 21 22   -1 0 1 | 1  2  1
'''
    