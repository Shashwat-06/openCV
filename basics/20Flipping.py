import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("image", img)
flipped = cv.flip(img, 1)
# 0 for vertical flip
# 1 for hoizontal flip 
# -1 for both veritcal and horizontol flip
cv.imshow("flipped", flipped)



cv.waitKey(0)