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

    haar_cascade = cv.CascadeClassifier("FaceDetection/haar_face.xml")

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    # cv.imshow("live video", frame)
    cv.imshow("gray video", frame)


    if cv.waitKey(1) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()