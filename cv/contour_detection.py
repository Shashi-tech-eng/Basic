#Contour detection using Canny
import cv2
import numpy as np
img=cv2.imread("bumble.png")
cann=cv2.Canny(img,125,255)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blank=np.zeros(img.shape,dtype='uint8')
blank1=np.zeros(img.shape,dtype='uint8')
thres=cv2.threshold(gray,121,255,cv2.THRESH_BINARY)[1]
contours,hierarchy=cv2.findContours(cann,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(blank,contours,-1,(0,0,255),thickness=1)
cv2.imshow("Draw Contours",blank)
print("Number of contours are ",len(contours))

cont,hierarchy=cv2.findContours(image=thres,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_SIMPLE)
print(len(cont))
cv2.drawContours(image=blank1,contours=cont,contourIdx=-1,color=(0,0,255),thickness=2)
cv2.imshow("Thres",blank1)

cv2.waitKey(0)
cv2.destroyAllWindows()
