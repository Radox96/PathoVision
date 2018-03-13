import cv2
import numpy as np

path = "/github/PathoCV/test_img/test.jpg"


im = cv2.imread(path)
#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im,contours,-1,(0,255,0),3)

#End of Code

