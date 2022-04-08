import cv2
import numpy as np
img = np.ones((400,600,3),np.uint8)*125

y=int(img.shape[1]/2)
x=int(img.shape[0]/2)
cv2.circle(img,(y,x),30,(255,0,255),-1)
flag=1
for i in range(40,200,20):
    cv2.circle(img,(y,x),i,(255,255,0),2)
while 1:
    if flag==1:
        for i in range(40,200,20):
            cv2.circle(img,(y,x),i,(0,255,255),2)
            cv2.imshow('',img)
            if cv2.waitKey(100)!=-1:
                flag=-1
                break
        flag=0
    else:
        for i in range(200,40,-20):
            cv2.circle(img,(y,x),i-20,(242,12,35),2)
            cv2.imshow('',img)
            if cv2.waitKey(100)!=-1:
                flag=-1
                break
        flag=1
cv2.waitKey(0)
