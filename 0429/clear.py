import cv2
import numpy as np
from scipy.fft import dst

src = cv2.imread("hung.jpg")
dst=cv2.medianBlur(src,3)
cv2.imshow("src",src)
cv2.imshow("result",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
