# just messing around to see how canny would look on live 

import cv2 as cv
import numpy as np
capture = cv.VideoCapture(0)
# cv.imshow("person", img)


# cv.imshow("canny", canny)

# def changeRes(width, height):
#     capture.set(3,width)
#     capture.set(4,height)

# changeRes(640,480)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3,3), 0)
    edges = cv.Canny(blur, 50, 120)
    # edges = cv.Canny(blur, 100, 200)

    blue_edges = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)
    blue_edges[edges != 0] = (0, 0, 255)

    # cv.imshow("live video", frame)
    cv.imshow("gray video", blur)
    cv.imshow("canny video", blue_edges)

    if cv.waitKey(1) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()