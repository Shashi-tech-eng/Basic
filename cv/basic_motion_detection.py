import cv2
import numpy as np
cap=cv2.VideoCapture("people.mp4")
while cap.isOpened():
    ret,frame1=cap.read()
    ret,frame2=cap.read()
    rframe1=cv2.resize(frame1,(1000,700),interpolation=cv2.INTER_AREA)
    rframe2=cv2.resize(frame2,(1000,700),interpolation=cv2.INTER_AREA)
    diff=cv2.absdiff(rframe1,rframe2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(9,9),0)
    _,thres=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thres,None,iterations=5)
    contours,_=cv2.findContours(dilated,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(rframe1,contours,-1,(0,255,0),2)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<3000:
            continue
        else:
            cv2.rectangle(rframe1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Inter",rframe1)
    frame1=frame2
    frame2=cap.read()
    if cv2.waitKey(40)==27:
        break
cap.release()
cv2.destroyAllWindows()
