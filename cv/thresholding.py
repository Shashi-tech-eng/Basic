import cv2
import matplotlib.pyplot as plt
im=cv2.imread("bumble.png")
img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,125,255)
#cv2.imshow("Canny",canny)
#Thresholding
thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)[1]
#cv2.imshow("Binary Threshold",thresh)

thresh1=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)[1]
#cv2.imshow("Binary Inverse Threshold",thresh1)

thresh2=cv2.threshold(gray,125,255,cv2.THRESH_TOZERO)[1]
#cv2.imshow("To Zero Threshold",thresh2)

thresh3=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)[1]
#cv2.imshow("To Zero Inverse Threshold",thresh3)

thresh4=cv2.threshold(gray,125,255,cv2.THRESH_OTSU)[1]
#cv2.imshow("Otsu Threshold",thresh4)

#Adaptive Thresholding
Adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,3)
#cv2.imshow("Adaptive Threshold",Adaptive)

titles=["Original","Canny","Binary Threshold","Binary Inverse Threshold","To Zero Threshold","To Zero Inverse Threshold","Otsu Threshold","Adaptive Threshold"]
images=[img,canny,thresh,thresh1,thresh2,thresh3,thresh4,Adaptive]
count=8
for i in range(count):
    plt.subplot(2,4,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()
plt.close()

cv2.waitKey(0)
cv2.destroyAllWindows()