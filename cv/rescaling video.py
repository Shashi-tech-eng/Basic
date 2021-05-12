import cv2
def rescale(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
capture=cv2.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    frame_resized=rescale(frame,scale=0.75)
    cv2.imshow("Original",frame)
    cv2.imshow("Resized",frame_resized)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
capture.release()
cv2.destroyAllWindows()