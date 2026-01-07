# rescale and resize for images

import cv2 as cv

img = cv.imread("Photos/cat_large.jpg")


def resiseImg(image, scale=0.5):
    width = int(image.shape[1]*scale)
    height = int(image.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

cv.imshow("img", img)
resized_img = resiseImg(img, scale=0.2)
cv.imshow("resized image", resized_img)
cv.waitKey(0)