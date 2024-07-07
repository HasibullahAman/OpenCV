import cv2 as cv
import numpy as np


img = cv.imread('images/baboon.png')
cv.imshow("baboon", img)


blanks = np.zeros((500,500), dtype = 'uint8')
cv.imshow('shape', blanks)

cv.waitKey(10000)