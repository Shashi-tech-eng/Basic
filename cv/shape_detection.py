import cv2
im=cv2.imread("shapes.jpg")
img=cv2.resize(im,(1000,500))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold",thres)
contours,_=cv2.findContours(thres,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),3)
    x=approx.ravel()[1]
    y=approx.ravel()[0] 
    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))
    elif len(approx) == 4:
        x1,y1,w,h=cv2.boundingRect(approx)
        aspect_ratio=float(w)/h
        if aspect_ratio>=0.95 and aspect_ratio<=1.05:
            cv2.putText(img,"Square",(x1,y1),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,"Rectangle",(x1,y1),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))
    elif len(approx) == 5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))   
    elif len(approx) == 10:
        cv2.putText(img,"Star",(x,y),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,0,0))
cv2.imshow("Shapes detected",img)
cv2.waitKey(0)
