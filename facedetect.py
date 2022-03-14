import cv2 as cv
import numpy as np

# img = cv.imread('Images/group 2.jpg')
# cv.imshow('Lady', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Lady', gray)


haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

# print('No of faces = ', len(faces_rect))


# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

# cv.imshow('Detected Face', img)

def detect(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 9)
    for (x,y,w,h) in face_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,200), thickness=2)

capture = cv.VideoCapture(0)
while True:
    istrue, frame = capture.read()
    frame = cv.flip(frame, 1)
    detect(frame)
    cv.imshow('Check', frame)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

# cv.waitKey(0)