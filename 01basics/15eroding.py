import cv2 as cv

image = cv.imread("Photos/park.jpg")
# cv.imshow("park", image)

blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)

# cv.imshow("blur", blur)

canny = cv.Canny(blur, 125, 175)
# cv.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
cv.imshow("canny", canny)


# dilating the image

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("dilated", dilated)

# eroding the image

eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Erroded", eroded)


cv.waitKey(0)

