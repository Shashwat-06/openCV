import cv2 as cv

image = cv.imread("Photos/cat.jpg")

cv.imshow("cat", image)

# converting to grayscale

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)


cv.waitKey(0)