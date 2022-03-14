import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']


# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

img = cv.imread(r'G:\development\OpenCV\Faces\val\elton_john\3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)


#Detect the face

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y: y+h, x:x+w]
    

    label, confidence = face_recognizer.predict(faces_roi)

    print('Label = ', people[label], '\nWith confidence of = ', confidence)

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), thickness = 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)


cv.imshow('Face recognized',img)


cv.waitKey(0)
