import cv2 as cv

image = cv.imread("Photos/park.jpg")
cv.imshow("park", image)

# resizing the image

resized = cv.resize(image, (500,500), cv.INTER_LINEAR)
cv.imshow("resized", resized)

cv.waitKey(0)

