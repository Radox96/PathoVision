import cv2 as cv
import numpy as np
import plantcv as pcv
import argparse as argp

#import via OpenCV
image = cv.imread("test_001.JPG")

height, width = image.shape[:2]

print height

#convert to grayscale 
imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

height2, width2 = imgray.shape[:2]

print height2

#set theshold
ret, thresh = cv.threshold(imgray, 127, 255, 0)
#find contours 
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#draw contours 
cv.drawContours(imgray, contours, -1, (0,255,0), 3)
#wirte image 
cv.imwrite("testresult2.jpg", imgray)

#End of Code


