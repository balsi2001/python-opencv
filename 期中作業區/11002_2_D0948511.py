import cv2
import time
import numpy as np
def circle_draw():
    h=400
    w=600
    img=np.ones((400,600,3),np.uint8)*125
    y=int(img.shape[0]/2)
    x=int(img.shape[1]/2)
    imgs=[]

    for i in range(40,200,np.random.randint(1,5)):
        tx=np.random.randint(50,520)
        ty=np.random.randint(50,350)
        tz=np.random.randint(10,50)
        cv2.circle(img,(tx,ty),tz,np.random.randint(0,256,size=3).tolist(),2)
        imgs.append(img.copy())
        cv2.circle(img,(tx,ty),tz,(125,125,125),2)
        imgs.append(img.copy())
    flag=0
    while flag==0:
        if flag==1:
            break
        for i in imgs:
            if flag==1:
                break
            cv2.imshow('',i)
            time.sleep(0.1)
            k=cv2.waitKey(400)
            if k==13 or k==32:
                if k==13:
                    cv2.destroyAllWindows()
                    flag=1
                    break
                elif k==32:
                    while 1:
                      k=cv2.waitKey() 
                      if k==13:
                          flag=1
                          break
                      if k==32:
                          break   
        imgs.reverse()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
circle_draw()