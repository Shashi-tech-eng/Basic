import numpy as np
import cv2
img=cv2.imread('shapes.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,9, 3, 0.04)
dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=(0,255,0)
cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()