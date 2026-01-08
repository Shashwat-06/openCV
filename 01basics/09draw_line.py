import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1)
cv.imshow("line", blank)

cv.waitKey(0)
