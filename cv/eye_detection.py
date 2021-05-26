import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture('sample.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    #frame=rescale(fra,0.75)
    frame=cv2.resize(frame,(1000,700))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,9)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.2,7)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,0,255))
    cv2.imshow('img', frame)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.destroyAllWindows()
