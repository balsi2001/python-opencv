import cv2
import numpy as np
from sklearn.metrics import zero_one_loss
src = cv2.imread("minnesota.jpg",cv2.IMREAD_GRAYSCALE)     
thresh = 127                                            
maxval = 255      
                                        
ret,binary = cv2.threshold(src,thresh,maxval,cv2.THRESH_BINARY)    
ret,zero= cv2.threshold(src,thresh,maxval,cv2.THRESH_TOZERO)   
ret,zeroinv= cv2.threshold(src,thresh,maxval,cv2.THRESH_TOZERO_INV)   
meanc = cv2.adaptiveThreshold(src,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY,3,5)
gauss = cv2.adaptiveThreshold(src,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY,3,5)
cv2.imshow("src",src)                                   
cv2.imshow("THRESH_BINARY",binary)                         
cv2.imshow("ADAPTIVE_THRESH_MEAN_C",meanc)          
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",gauss)  
cv2.imshow("THRESH_TOZERO",zero)   
cv2.imshow("THRESH_TOZERO_INV",zeroinv)    
cv2.waitKey(0)
cv2.destroyAllWindows() 