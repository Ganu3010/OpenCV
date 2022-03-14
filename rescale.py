import cv2 as cv
def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    # changeres(0.5,0.5)
    cv.imshow('Large',frame)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break
    # if cv.waitKey(0):
    #     break
capture.release()
cv.destroyAllWindows()

