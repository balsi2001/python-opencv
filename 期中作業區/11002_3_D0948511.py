import cv2
import numpy as np
h=400
global b0b1
b0b1=0
w=500
events = [i for i in dir(cv2) if "EVENT" in i]
for e in events:
    print(e)

cr=0    
img=np.ones((h,w,3),np.uint8)*255
def pa():
    pass
def act(event,x,y,flags,param):

    
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),cr,(b,g,r),2)
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),cr,(b,g,r),-1)
    if flags==9:
        cv2.rectangle(img,(x,y),(x+cr,y+cr),(b,g,r),-1)
    #print(event)
    #print(flags)
r=0
b=0
g=0
cv2.namedWindow('draw circle or rectangle')
cv2.setMouseCallback('draw circle or rectangle',act)
cv2.createTrackbar('r','draw circle or rectangle',0,255,pa)
cv2.createTrackbar('g','draw circle or rectangle',0,255,pa)
cv2.createTrackbar('b','draw circle or rectangle',0,255,pa)
cv2.createTrackbar('radius','draw circle or rectangle',4,60,pa)
cv2.createTrackbar('0/1','draw circle or rectangle',0,1,pa)
while 1:
    cv2.imshow('draw circle or rectangle',img)
    r=cv2.getTrackbarPos('r','draw circle or rectangle')
    g=cv2.getTrackbarPos('g','draw circle or rectangle')
    b=cv2.getTrackbarPos('r','draw circle or rectangle')
    cr=cv2.getTrackbarPos('radius','draw circle or rectangle')
    b0b1=cv2.getTrackbarPos('0/1','draw circle or rectangle')
    key=cv2.waitKey(100)
    #print(key)
    if key==ord('Q')or key ==ord('q'):
        break
rr=cv2.imwrite('myidea_D0948511.jpg', img)

cv2.destroyAllWindows()
#def act(event,x,y,flags,param):
