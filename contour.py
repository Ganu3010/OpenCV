import cv2 as cv
import numpy as np

# capture = cv.VideoCapture(0)

# while True:
#     istrue, frame = capture.read()
#     frame = cv.flip(frame, 1)
#     c = cv.Canny(frame, 90, 200)
#     cv.imshow('Camera', c)
#     cv.imshow('Camera1', frame)
#     if cv.waitKey(30) & 0xFF == ord('x'):
#         break

# capture.release()
# cv.destroyAllWindows()

img = cv.imread('Images/cat.jpg')
c = cv.Canny(img, 125, 175)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)
cv.imshow('OG', img)
cv.imshow('Canny', c)
cv.waitKey(0)