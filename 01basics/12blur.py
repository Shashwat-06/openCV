import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("park",img)

# blur

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# cv.GaussianBlur(src, ksize, sigmaX, sigmaY=None, borderType=None)

cv.waitKey(0)