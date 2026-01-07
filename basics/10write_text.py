import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

# writing text 

cv.putText(blank, "hello world, I am shashwat", (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2 )
# cv.putText(image, text, org, fontFace, fontScale, color, thickness=None, lineType=None)


cv.imshow("text", blank)
cv.waitKey(0)