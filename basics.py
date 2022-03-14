import cv2 as cv

img = cv.imread('Images/park.jpg')
cv.imshow('Actual Image', img)
#Converting to Grayscale:

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Actual Image', img)
# cv.imshow('GrayScale Image', gray)
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('Camera',frame)
#     if cv.waitKey(20) & 0xFF == ord('x'):
#         break
# capture.release()
# cv.destroyAllWindows()

#Blurring Images:

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# # cv.imshow('Blurred', blur)
# # cv.imshow('Actual', img)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# dialated = cv.dilate(canny, (3, 3), iterations=3)
# cv.imshow('Dialated Image',dialated)

# eroded = cv.erode(dialated, (3,3), iterations=2)
# cv.imshow('Eroded', eroded)

resized = cv.resize(img, (200, 200))
cv.imshow('Resized',resized)

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
