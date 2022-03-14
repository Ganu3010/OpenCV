import cv2 as cv
import numpy as np

img = cv.imread('Images/cats.jpg')
cv.imshow('Actual', img)

blurred = cv.bilateralFilter(img, 5, 15, 75)
cv.imshow('Bilateral Filter', blurred)

cv.waitKey(0)
