import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#Paint certain color.
# blank[:] = 255,255,255
# cv.imshow('Green', blank)
cv.circle(blank, (50,50), 25, (255, 255, 255), thickness=1)
cv.putText(blank, "Bello", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), thickness=1)
cv.imshow("Text", blank)
cv.waitKey(0)