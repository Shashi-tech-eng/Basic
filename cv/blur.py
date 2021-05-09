import cv2
import matplotlib.pyplot as plt
im=cv2.imread("bumble.png")
img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
#Averaging Blur
blur1=cv2.blur(img,(5,5))
#Gaussian Blur 
blur2=cv2.GaussianBlur(img,(5,5),1)
#Median Blur
blur3=cv2.medianBlur(img,5)
#Bilateral Filtering
blur4=cv2.bilateralFilter(img,3,75,75)

titles=["Original","Averaging","Gaussian Blur","Median Blur","Bilateral Filter"]
images=[img,blur1,blur2,blur3,blur4]
count=5
for i in range(count):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()
plt.close()