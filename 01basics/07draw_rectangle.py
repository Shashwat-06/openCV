import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("blank", blank)

# Draw a rectangle
cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1) #to fill use thickness=cv.FILLED or thickness=-1
    #cv.rectangle takes image, pt1, pt2, color, thickness, lineType, shift as arguments 
    #image must be a numpy array,
    # pt1 is the top-left corner and pt2 is the bottom-right corner
    # color format is BGR not RGB
    # thickness - thickness of rectangular border
    # lineType - cv.LINE_8(default) , cv.LINE_AA(anti aliasing, smoother)
    # shift - used for fixed point coordinates
cv.imshow("rectangle", blank)


cv.waitKey(0)