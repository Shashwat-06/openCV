import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
# thresholding is a binarization of image, an image where pixels are zero(black) or 255(white) we set a threshold value if the pixel intensity is less than it we set it to zero or we set it to 255 white

# simple thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple threshold inverse", thresh_inv)


# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresholding", adaptive_thresh)



cv.waitKey(0)