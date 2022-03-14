import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (100, 100), (300, 300), (255, 0,0), -1)
# cv.imshow('Rectangle', rect)
circle = cv.circle(blank.copy(), (200, 200), 100, (255,0,0), -1)
cv.imshow('Circle', circle)

# cv.rectangle(rect, (300, 100), (400, 200), (255, 255, 255), -1)
cv.imshow('Rectangle', rect)

img_and = cv.bitwise_and(rect, circle)
img_or = cv.bitwise_or(rect, circle)
img_xor = cv.bitwise_xor(rect, circle)
img_not_rect = cv.bitwise_not(rect)
img_not_circle = cv.bitwise_not(circle)

cv.imshow('AND', img_and)
cv.imshow('OR', img_or)
cv.imshow('XOR', img_xor)
cv.imshow('NOT Rectangle', img_not_rect)
cv.imshow('NOT CIRCLE', img_not_circle)



cv.waitKey(0)