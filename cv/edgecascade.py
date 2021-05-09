import cv2
import numpy as np
img=cv2.imread("bumble.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,125,255)
cv2.imshow("Canny",canny)


#using threshold to detect less edges
Blur=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
Canny_blur=cv2.Canny(img,225,255)
cv2.imshow("Canny after blur",Canny_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()