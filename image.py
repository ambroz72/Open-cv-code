import cv2
img=cv2.imread('girl.jpg',0)
print(img)
cv2.imshow('image',img)
cv2.waitKey(10000)
cv2.destroyWindow()