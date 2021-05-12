import cv2
def rescale(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
img=cv2.imread("bumble.png")
frame_resized=rescale(img,0.75)
cv2.imshow("Resized",frame_resized)
cv2.waitKey(0)