import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank)

# draw a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1, lineType=cv.LINE_AA)

cv.imshow("circle", blank)



cv.waitKey(0)
