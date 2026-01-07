# rescale and resize for live video

import cv2 as cv

capture = cv.VideoCapture(0)#live video 

def changeRes(width, height):
    # can only be used for live videos 
    capture.set(3, width) #3 for width 
    capture.set(4, height) #4 for height

changeRes(640, 480)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    
    cv.imshow("resized_live_video", frame)

    if cv.waitKey(1) & 0xFF==ord("d"):
        break

capture.release()
capture.destroyAllWindow()

