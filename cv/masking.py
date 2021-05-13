import cv2
import numpy as np
img=cv2.imread("bumble.png")
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv2.rectangle(blank,(img.shape[1]//2-170,img.shape[0]//2-100),(img.shape[1]//2+150,img.shape[0]//2+100),255,-1)
masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("original",img)
cv2.imshow("mask",mask)
cv2.imshow("masked image",masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
