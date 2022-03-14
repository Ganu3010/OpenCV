import datetime as dt
import cv2 as cv
import numpy as np



# dto = dt.datetime.now()
# s = str(dto.hour)+str(dto.minute)+str(dto.second)

# capture = cv.VideoCapture(0)

# while True:
#     dto = dt.datetime.now()
#     s = str(dto.hour)+str(dto.minute)+str(dto.second)
#     s+='m.jpg'
#     s = 'Manas/'+s
#     frame, istrue = capture.read()
#     cv.imwrite(s,frame)
#     cv.waitKey(600000)
#     if cv.waitKey(20) and 0xFF == ord('x'):
#         break


img = cv.imread('Manas/18285m.jpg')
cv.imshow('Manas', img)


cv.waitKey(0)


