import cv2 as cv
import numpy as np
img = cv.imread('Images/park.jpg')

cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

#Laplacian Gradient Detection

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Image', lap)

# blur = cv.GaussianBlur(gray, (7,7), 0)
#Sobel Gradient Detection
sobx = cv.Sobel(gray, cv.CV_64F, 1, 0)
soby = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('Sobel X', sobx)
# cv.imshow('Sobel Y', soby)

combine = cv.bitwise_or(sobx, soby)

cv.imshow('Sobel', combine)

cv.imshow('Canny Edge', cv.Canny(gray, 125, 155))

cv.waitKey(0)