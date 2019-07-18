import cv2
img = cv2.imread("Green_bird.jpg",1)
cv2.imshow("Title",img)
# resizeImg = cv2.resize(img(400,400))
shape=img.shape
resizeImg = cv2.resize(img,(shape[0]//2, shape[1]//2))
cv2.imshow("Title",resizeImg)
cv2.imwrite("MyGreenBird.jpg",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()