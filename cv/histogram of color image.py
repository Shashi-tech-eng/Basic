import cv2
import matplotlib.pyplot as plt
img=cv2.imread("bumble.png")
cv2.imshow("Color image",img)
colors=('b','g','r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for i,col in enumerate(colors):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
