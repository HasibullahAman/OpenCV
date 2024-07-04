import cv2 as cv




def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] ==> width of image
    height = int(frame.shape[0] * scale) # frame.shape[0] ==> height of image
    
    dimenations = (width,height)
    
    return cv.resize(frame,dimenations, interpolation = cv.INTER_AREA)



# read image
# frame = cv.imread("images/cat.png")
# resize_frame = rescaleFrame(frame) # we resize the image here
# cv.imshow("cat",resize_frame)
# cv.imshow("same_cat",frame)
# cv.waitKey(0 )



# read Video  

video = cv.VideoCapture("video/B.mp4")


while True:
    isTrue, frame = video.read()
    resize_frame = rescaleFrame(frame)
    
    cv.imshow("Video",resize_frame)
    cv.imshow("Video_original",frame)
    
    
    
    if cv.waitKey(20) &  0xFF==ord('q'):
        break
    
video.release()
cv.destroyAllWindows()
    
