import cv2 as cv

image = cv.imread("Photos/park.jpg")
cv.imshow("original image", image)

cropped = image[50:200, 200:400]
cv.imshow("cropped image", cropped)


cv.waitKey(0)