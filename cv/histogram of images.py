import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("bumble.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",gray)
hist=cv2.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title("Histogram of Grayscale image")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()


