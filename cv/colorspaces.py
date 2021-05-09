import cv2
import numpy as np
img=cv2.imread("bumble.png")
# Original
cv2.imshow("Original",img)
#BGR to Gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)
#BGR to HSV
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",HSV)
#BGR to LAB
LAB=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",LAB)


cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,frame=cap.read()
    HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",HSV)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()