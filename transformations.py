import cv2 as cv
import numpy as np

# img = cv.imread('Images/park.jpg')

# # cv.imshow('Actual Image', img)
def rotate(img, angle,rotpoint = None):
    (height, width) = img.shape[:2]
    if rotpoint == None:
        rotpoint = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1)
    dimensions = (width, height)
    return cv.warpAffine(img, rotmat, dimensions)


def resize(frame, scale):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



capture = cv.VideoCapture(0)
i = 0
j = 2
c = True
while True:
    istrue, frame = capture.read()
    scale = resize(frame, j)
    rotated = rotate(scale, i)
    # frame = cv.flip(frame, 1)
    # cv.putText(frame, 'Manas Sewatkar', (frame.shape[1]//2, frame.shape[0]//2), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), thickness=2)
    cv.imshow('Camera', rotated)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break
    i+=1
    if c:
        j*=0.999
    else:
        j/=0.999
    if j<0.1:
        c = False
    if j >2:
        c = True

capture.release()
cv.destroyAllWindows()