import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

img = cv.imread("Photos/park.jpg")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# bitwise AND this gives intersection of both images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise AND ", bitwise_and)

# bitwise OR this gives union of both images(both intersecting and non intersecting region)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise OR", bitwise_or)

# bitwise XOR this gives non intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise XOR", bitwise_xor)

# bitwise NOT this inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("rectangle not", bitwise_not)

cv.waitKey(0)