import cv2 as cv




def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale) # frame.shape[1] ==> width of image
    height = int(frame.shape[0] * scale) # frame.shape[0] ==> height of image
    
    dimenations = (width,height)
    
    return cv.resize(frame,dimenations, interpolation = cv.INTER_AREA)


