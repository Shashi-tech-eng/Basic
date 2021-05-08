import cv2
cap=cv2.VideoCapture(0)
#Captures webacam of your desktop
while True:
    _,frame=cap.read()
    #capture frames from video stream
    cv2.imshow("Original",frame)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.destroyAllWindows()