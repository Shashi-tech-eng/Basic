import cv2
import numpy as np

img=cv2.imread("bumble.png")
#cv2.imshow("Original",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,125,255)
cv2.imshow("Canny",canny)
#Erosion 
erosion=cv2.erode(canny,(3,3),iterations=1)
cv2.imshow("erosion",erosion)
#Dilation
dilation=cv2.dilate(canny,(3,3),iterations=1)
cv2.imshow("dilation",dilation)

bit=cv2.bitwise_and(gray,erosion)
cv2.imshow("bit",bit)
cv2.waitKey(0)
cv2.destroyAllWindows()
