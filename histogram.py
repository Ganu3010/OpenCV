import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('Images/cats.jpg')


cv.imshow('Cat', img)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #Gray Histogram
# gray_hist = cv.calcHist([gray], [0], None, histSize=[256], ranges=[0,256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


colors = ('b', 'g', 'r')

plt.figure()
plt.title("Color Histogram")
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256]) # list of images, color channel, max limit (list), range of x-axis var.
    plt.plot(hist, color = col) 
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)