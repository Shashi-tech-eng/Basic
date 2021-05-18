import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2 
def rescale(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

def region_of_interest(img, vertices):
    # Define a blank matrix that matches the image height/width.
    mask = np.zeros_like(img)
    # Retrieve the number of color channels of the image.
    #channel_count = img.shape[2]
    # Create a match color with the same color channel counts.
    match_mask_color = 255
      
    # Fill inside the polygon
    cv2.fillPoly(mask, vertices, match_mask_color)
    
    # Returning the image only where mask pixels match
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
def draw_lines(img,lines):
    img=np.copy(img)
    blank_image=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0),thickness=3)
    img=cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img
def process(img):
    #im=cv2.imread("Roads_resized.jpg")
    #img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    width=img.shape[0]
    height=img.shape[1]
    roi_vertices=[
        (0,width),
        (height/2,width/2),
        (height,width),
    ]
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_image=cv2.Canny(gray, 100, 200)
    cropped_image=region_of_interest(canny_image, np.array([roi_vertices],np.int32))
    cv2.imshow("Cropped image",cropped_image)
    lines=cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/180, threshold=50,lines=np.array([]),minLineLength=100,maxLineGap=100)
    image_with_lines=draw_lines(img, lines)
    return image_with_lines
cap=cv2.VideoCapture("lane_on_roads.mp4")
while cap.isOpened():
    ret,frame=cap.read()
    frame_resized=rescale(frame,scale=0.50)
    frame_resized=process(frame_resized)
    cv2.imshow('frame', frame_resized)
    if cv2.waitKey(20) & 0xFF==ord('f'):
        break
cap.release()
cv2.destroyAllWindows()



