import cv2 as cv

img = cv.imread('.\images/baboon.png')
cv.imshow('Cat', img)
cv.waitKey(0)
