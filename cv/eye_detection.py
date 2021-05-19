import cv2
import numpy as np
def rescale(frame,scale):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,fra=cap.read()
    frame=rescale(fra,0.75)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0))
    cv2.imshow('img', frame)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.destroyAllWindows()
