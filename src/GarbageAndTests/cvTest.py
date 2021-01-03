import cv2

img = cv2.imread("A2.png")
print(img)
cv2.imshow("Title", img)
cv2.waitKey(0)