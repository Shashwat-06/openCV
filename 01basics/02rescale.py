# Resizing and Rescaling
import cv2 as cv

capture = cv.VideoCapture("Videos/dog.mp4")

def rescaleFrame(frame, scale=0.75):
    # can be used for images, videos and live videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow("video", frame)
    cv.imshow("resized video", frame_resized)#for static videos
    
    if cv.waitKey(1) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()

