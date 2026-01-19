# gradients
import cv2 as cv
import numpy as np
img = cv.imread("Photos/park.jpg")
cv.imshow("park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow("laplasian", lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F,1,0)
sobely = cv.Sobel(gray, cv.CV_64F,0,1)
combined = cv.bitwise_or(sobelx, sobely)

cv.imshow("sobel X", sobelx)
cv.imshow("sobel Y", sobely)
cv.imshow("combined", combined)


canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)




cv.waitKey(0)


