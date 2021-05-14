import cv2
img=cv2.imread("bumble.png")
G = img.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    cv2.imshow(str(i),G)
    gpA.append(G)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
