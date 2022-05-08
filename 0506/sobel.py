import cv2
import numpy as np
src = cv2.imread('lena.jpg',0)

cv2.imshow("Src", src)
org1=np.zeros(src.shape,np.uint8)
n=src
#gx=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
gx=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
#gx=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
gx=np.array(gx)
#gy=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
gy=[[-1, -2,-1], [0, 0, 0],[1,2,1]]
#gy=[[-1, 0,1], [-2, 0, 2],[-1,0,1]]
gy=np.array(gy)

gg=np.array([[0,0],[1,1],[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]])

tx=0
ty=0
for i in range(1,323):
    t=0
    x=0
    y=0
    for j in range(1,320):
        x=0
        y=0
        for k,l in gg:
            x+=(n[i+k,j+l]*gx[1+k,1+l])
            y+=(n[i+k,j+l]*gy[1+k,1+l])
        t=(((x)**2)+((y)**2))**0.5
        org1[i][j]=t

cv2.imshow('org',org1)
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

    