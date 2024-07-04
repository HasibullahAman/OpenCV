import cv2 as cv

# img = cv.imread('.\images/baboon.png')

# cv.imshow('Cat', img)
# cv.waitKey(0)



capture = cv.VideoCapture('video/B.mp4')
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
        
    if cv.waitKey(20) &  0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()

    