import cv2
'''請讀取myhand.jpg, 請建立影像的輪廓 (二值化門檻值設50)
'''
src = cv2.imread("hand.jpg")
cv2.imshow("src",src)                               

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)    
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,50,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_SIMPLE)  
dst = cv2.drawContours(src, contours,-1,(0,255,0),5) 
cv2.imshow("result",dst)                            

cv2.waitKey(0)
cv2.destroyAllWindows()
