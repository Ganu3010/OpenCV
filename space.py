import cv2 as cv
import numpy as np 

# capture=cv.VideoCapture(0)
# while True:
#     istrue, frame = capture.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
#     cv.imshow('Camera', frame)
#     if cv.waitKey(30) & 0xFF == ord('x'):
#         break
# capture.release()
# cv.destroyAllWindows()

img = cv.imread('Images/park.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Actual',img)
cv.imshow('HSV', hsv)
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV - BGR', bgr)
cv.waitKey(0)