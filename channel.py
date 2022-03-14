import cv2 as cv
import numpy as np
img = cv.imread('Images/park.jpg')
cv.imshow('Actual Image', img)
e = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)
b = cv.merge([b,e,e])
g = cv.merge([e,g,e])
r = cv.merge([e,e,r])
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)



cv.waitKey(0)
