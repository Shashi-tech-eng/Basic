import cv2
import numpy as np
img=cv2.imread("thanos.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template=cv2.imread("template.jpg",0)
w,h=template.shape[::-1]
res=cv2.matchTemplate(gray, template,cv2.TM_CCOEFF_NORMED)
print(res)
threshold=0.99
loc=np.where(res >= threshold)
for pts in zip(*loc[::-1]):
    cv2.rectangle(img, pts, (pts[0]+w,pts[1]+h),(0,255,0),2)
print(loc)
#cv2.imshow("Original",img)
cv2.imwrite("Template matched.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()