import cv2 as cv

img = cv.imread("images/cat.png")
def rescaleFunction(frame,scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

changeFrame = rescaleFunction(img,0.75)
cv.imshow("changeFrame",changeFrame)

# change JPG image to Grayscale format
Gray = cv.cvtColor(changeFrame,cv.COLOR_RGB2GRAY)
cv.imshow("grayImage",Gray)


# Blur image

blur = cv.GaussianBlur(changeFrame,(7,7),cv.BORDER_DEFAULT)
cv.imshow("blurImage",blur)

# Edge Cascade
canny = cv.Canny(changeFrame,125,175)
cv.imshow("cannyImage",canny)


cv.waitKey(20000)