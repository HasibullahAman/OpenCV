import cv2 as cv
import numpy as np


# read image
# img = cv.imread('images/baboon.png')
# cv.imshow("baboon", img)

# create blank image
blanks = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('shape', blanks)

# paint the image a certain color
# Green
# blanks[:] = 0,255,0
# cv.imshow('Green', blanks)


# Red
# blanks[:] = 0,0,255
# cv.imshow('Green', blanks)


# if I want half of the image
blanks[200:300, 200:300] = 0,0,255
cv.imshow("halfRed", blanks)


cv.waitKey(10000)