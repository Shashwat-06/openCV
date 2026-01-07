import cv2 as cv

image = cv.imread("Photos/park.jpg")
# cv.imshow("park", image)

blur = cv.GaussianBlur(image, (3,3), cv.BORDER_DEFAULT)

# cv.imshow("blur", blur)

# edge cascading

canny = cv.Canny(image, 125, 175)
# cv.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
cv.imshow("canny", canny)

cv.waitKey(0)

