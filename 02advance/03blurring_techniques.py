import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats", img)

# Averaging

average = cv.blur(img, (3,3))
cv.imshow("average blur", average)

# gaussian blur

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("gaussian blur", gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 10)
cv.imshow("bilateral blur", bilateral)


cv.waitKey(0)