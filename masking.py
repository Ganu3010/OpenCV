import cv2 as cv
import numpy as np

# img = cv.imread('Images/park.jpg')
# blank = np.zeros(img.shape[:2], dtype='uint8')

# cv.imshow('Actual Image', img)

# rect = cv.rectangle(blank.copy(), (img.shape[1]//4, img.shape[0]//4), (3*img.shape[1]//4, 3*img.shape[0]//4), (255,0,0), -1)

# rect = cv.bitwise_not(rect)
# masked = cv.bitwise_and(img, img, mask=rect)

# cv.imshow('Masked Image', masked)




# cv.waitKey(0)
def mask(frame):
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    c = cv.circle(blank, (frame.shape[1]//2, frame.shape[0]//2), 100, (255,0,0), -1)
    masked = cv.bitwise_and(frame, frame, mask = c)
    return masked
capture = cv.VideoCapture(0)

while True:
    istrue, frame = capture.read()
    masked = mask(frame)
    display = cv.flip(masked, 1)
    cv.imshow('Masked Camera', display)

    if cv.waitKey(10) & 0xFF == ord('x'):
        break

capture.release()
cv.destroyAllWindows()