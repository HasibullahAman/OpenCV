import numpy as np
# how basic we read image
import cv2 as cv
img = cv.imread('images\cat.png')
cv.imshow('cat', img)
cv.waitKey(0)
