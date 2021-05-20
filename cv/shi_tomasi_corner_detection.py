import numpy as np
import cv2
def shi_tomasi(img):
    #img=cv2.imread('ironman.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners=cv2.goodFeaturesToTrack(gray, 200, 0.01,5)
    corners =np.int0(corners)
    for i in corners:
        x,y=i.ravel()
        cv2.circle(img, (x,y),1,(0,0,255),-1)
    return img
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    dst=shi_tomasi(frame)
    cv2.imshow('Corners detected', dst)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.destroyAllWindows()