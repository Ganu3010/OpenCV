import cv2 as cv
import numpy as np
img = cv.imread('Images/ss.png')

# cv.imshow('Screenshot', img)

def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
img2 = rescale(img, 0.5)

# cv.imshow('Reduced SS', img2)
# gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)



# b,g,r = cv.split(img2)
# e = np.zeros(img2.shape[:2], dtype='uint8')
# b = cv.merge([b,e,e])
# g = cv.merge([e,g,e])
# r = cv.merge([e,e,r])

# cv.imshow('Blue SS', b)
# cv.imshow('Green SS', g)
# cv.imshow('Red SS', r)
# cv.imshow('Gray SS', gray)


c = cv.Canny(img2, 10, 175)

cv.imshow('Canny SS', c)


cv.waitKey(0)