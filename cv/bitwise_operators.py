import numpy as np
import cv2
blank=np.zeros((300,300),dtype="uint8")
rectangle=cv2.rectangle(blank.copy(),(150,150),(300,300),255,-1)
circle=cv2.circle(blank.copy(),(150,150),150,255,-1)
#bitwise and
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow("bitwise_and",bitwise_and)
#bitwise or
bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow("bitwise_or",bitwise_or)
#bitwise xor
bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow("bitwise xor",bitwise_xor)
#bitwise not
bitwise_not=cv2.bitwise_not(rectangle)
cv2.imshow("bitwise not",bitwise_not)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()

