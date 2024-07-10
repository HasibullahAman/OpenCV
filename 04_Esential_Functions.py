import cv2 as cv

img = cv.imread("images/cat.png")
def rescaleFunction(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

changeFrame = rescaleFunction(img,0.75)
cv.imshow("changeFrame",changeFrame)

cv.waitKey(20000)