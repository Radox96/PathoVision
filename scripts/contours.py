import cv2
import numpy as np

#define image path
path = "/github/PathoCV/test_img/test_001.JPG"

#load image
im = cv2.imread(path, 0)

#convert to grayscale (already done with above addition of ",0")
#imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#set threshold
ret, thresh = cv2.threshold(im, 127, 255, 0)

#generate contours
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
cv2.drawContours(im2, contours, -1, (0,255,0), 3)

#write results image
cv2.imwrite('result.jpg',im2)

#End of Code

