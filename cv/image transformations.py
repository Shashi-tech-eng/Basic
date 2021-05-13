import cv2
import numpy as np
img=cv2.imread("bumble.png")
#Translation
def translate(img,x,y):
  Translation_matrix=np.float32([[1,0,x],[0,1,y]])
  dimensions=(img.shape[1],img.shape[0])
  return cv2.warpAffine(img,Translation_matrix,dimensions)
translated=translate(img,50,50)
cv2.imshow("Translated",translated)

#Rotation
dimensions=(img.shape[1],img.shape[0])
rotation_point=(100,100)
angle=45
scale=1.0
translation_matrix=cv2.getRotationMatrix2D(rotation_point,angle,scale)
rotated=cv2.warpAffine(img,translation_matrix,dimensions)
cv2.imshow("Rotated",rotated)
#Flipping
flip=cv2.flip(img,-1)
cv2.imshow("Flipped",flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
