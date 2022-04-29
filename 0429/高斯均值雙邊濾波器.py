import cv2
src=cv2.imread("unistar.jpg")
cv2.imshow('src1',src)
d5=(5,5)
d7=(7,7)
ds5b=cv2.blur(src,d5)
ds5g=cv2.GaussianBlur(src,d5,0,0)
ds5b2_120=cv2.bilateralFilter(src,5,120,120)
cv2.imshow('src2',src)
cv2.imshow('ds5b',ds5b)
cv2.imshow('ds5g',ds5g)
cv2.imshow('ds5b2_120',ds5b2_120)
ds7b=cv2.blur(src,d7)
ds7g2=cv2.GaussianBlur(src,d7,0,0)
ds7g3=cv2.GaussianBlur(src,d5,0,0)
ds7g4=cv2.GaussianBlur(src,d5,0,0)

ds7b2_50=cv2.bilateralFilter(src,7,50,50)
cv2.imshow('ds7b',ds7b)
cv2.imshow('ds7g',ds7g2)
cv2.imshow('ds7b2_50',ds7b2_50)
ds5b2_50=cv2.bilateralFilter(src,5,50,50)
ds7b2_120=cv2.bilateralFilter(src,7,120,120)
cv2.imshow('ds5b2_50',ds5b2_50)
cv2.imshow('ds7b2_120',ds7b2_120)
cv2.imshow('src3',src)
cv2.imshow('src4',src)
cv2.imshow('srcg2',ds7g2)
cv2.imshow('srcg3',ds7g3)
cv2.imshow('srcg4',ds7g4)
cv2.waitKey(0)