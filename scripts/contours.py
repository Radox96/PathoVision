import cv2
import numpy as np

path = "/github/PathoCV/test_img/test_001.JPG"


im = cv2.imread(path, 0)
#imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(im, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imwrite('result.jpg',im2)
#cv2.writeimg('results.jpg', cv2.drawContours(im2,contours,-1,(0,255,0),3))

#End of Code

