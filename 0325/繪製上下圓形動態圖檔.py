from tkinter import W
import numpy as np
import cv2
import PIL
import time
width=640
height=480
r=15
speed=0.01
x=50
y=50
x_S=5
y_S=5
while cv2.waitKey(1)==-1:
    if x>width-r or r>x:
        x_S=-x_S
    if y>height-r or r>y:
        y_S=-y_S
    x+=x_S
    y+=y_S
    img=np.ones((height,width,3),np.uint8)*255
    cv2.circle(img,(x,50),r,(255,0,0),-1)
    cv2.circle(img,(50,y),r,(255,0,0),-1)
    cv2.imshow("",img)
    time.sleep(speed)
cv2.destoryAllWindows()