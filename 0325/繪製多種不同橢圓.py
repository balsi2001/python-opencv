import cv2
import numpy as np



'''def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)



img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
print(ascii('ESC'))
while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()'''
img = np.zeros((480, 600, 3), np.uint8)
x=int(img.shape[0]/2)
y=int(img.shape[1]/2)
for i in range(0,20):
    angle=np.random.randint(0,361)
    color=np.random.randint(0,256,size=4).tolist()
    cv2.ellipse(img,(y,x),(np.random.randint(0,100),np.random.randint(0,200)),angle,0,360,color,np.random.randint(0,5))
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()