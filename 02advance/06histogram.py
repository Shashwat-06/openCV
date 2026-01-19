import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# grayscale histogram

gray_hist = cv.calcHist([gray],[0], None, [256], [0,256])

plt.figure()
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("No. of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# color histogram
plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("No. of pixels")
colors = ("b","g","r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)