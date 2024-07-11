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


# Dilating the image
dilated = cv.dilate(canny,(7,7),iterations = 3)
cv.imshow("dilated",dilated)


# Eroded image

eroded = cv.erode(dilated,(7,7),iterations = 3)
cv.imshow("eroded",eroded)


# Resize the image
resized = cv.resize(img,(250,250))
cv.imshow("resizedImage",resized)

# Cropped image
cropped = img[50:200,200:500]
cv.imshow("croped",cropped)


cv.waitKey(20000)