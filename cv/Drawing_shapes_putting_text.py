import cv2
import numpy as np
blank=np.ones((512,512,3),dtype='uint8')
#Drawing rectangle 
cv2.rectangle(blank,(0,0),(256,256),(255,212,125),-1)
#Drawing circle
cv2.circle(blank,(256,256),128,(0,0,255),-1)
#Drawing Line
cv2.line(blank,(256,256),(512,512),(0,255,0),2)
#Putting text
cv2.putText(blank,"Added Text!!",(400,400),cv2.FONT_HERSHEY_PLAIN,1.0,(255,255,125),1)
cv2.imshow("Image",blank)
cv2.waitKey(0)