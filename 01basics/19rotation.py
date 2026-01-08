import cv2 as cv 

image = cv.imread("Photos/park.jpg")
cv.imshow("image", image)

# rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(image, 30)

cv.imshow("rotated",rotated)

cv.waitKey(0)