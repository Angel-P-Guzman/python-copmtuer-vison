import cv2 as cv

img = cv.imread('photos/cat.jpg')
#do the filter with an image first then we move on to video
# problems with video: 
# the input and differences between. For example, what if two different webcams are plugged in togheter, the names of the webcams. we do not want admin access. 
# then the refresh rate of the camera
# and computing the live video feed   
cv.imshow('cat', img)
cv.waitKey(0)