import cv2
import numpy as np
img=cv2.imread("door.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(9,9),0)
edges=cv2.Canny(blur,70,150,apertureSize=3)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("Edges",edges)
cv2.imshow("Transform",img)
cv2.waitKey(0)