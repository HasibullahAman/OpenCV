import cv2 as cv


img = cv.imread('images/baboon.png')
cv.imshow("Baboon",img)
cv.waitkey(0)