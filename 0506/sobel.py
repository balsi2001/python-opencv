from hashlib import sha1
import cv2
import numpy as np
src = cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow("Src", src)



org=np.zeros((int(src.shape[0]+1),int(src.shape[1]+1)),np.uint8)

dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)  # 影像融合
cv2.imshow("Dst", dst)

gx=np.array([[-1, 0,1], [-2, 0, 2],[-1,0,1]])
gy=np.array([[-1, -2, -1], [0, 0, 0],[1,2,1]])

print(src.shape[0],src.shape[1])
for i in range(1,src.shape[0]-1):
    t=0
    x=0
    y=0
    for j in range(1,src.shape[1]-1):
        x+=src[i-1,j-1]*-1
        x+=src[i,j-1]*-2
        x+=src[i+1,j-1]*-1
        x+=src[i-1,j+1]*1
        x+=src[i,j+1]*2
        x+=src[i+1,j+1]*1
        
        y+=src[i-1,j-1]*-1
        y+=src[i,j-1]*-2
        y+=src[i+1,j-1]*-1
        y+=src[i-1,j+1]*1
        y+=src[i,j+1]*2
        y+=src[i+1,j+1]*1
        t=((x**2)+(y**2))**0.5
        if t>=255:
            org[i,j]=255
        else:
            org[i,j]=t

cv2.imshow('org',org)
cv2.waitKey(0)
cv2.destroyAllWindows()
