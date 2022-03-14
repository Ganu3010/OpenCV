import cv2 as cv
import numpy as np

img = cv.imread('Images/cats.jpg')
cv.imshow('Actual Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)


#Simple Threshold
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)

cv.imshow('Simple Inverse Threshold', thresh_inv)




#Adaptive Threshold

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
#source, maxvalue, method, type of thresholding, block size (int), number which you wanna subtract from the mean to fine tune the image
cv.imshow('Adaptive Thresholding', adaptive_thresh)

adaptive_thresh_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Gaussian Thresholding', adaptive_thresh_gauss)



cv.waitKey(0)