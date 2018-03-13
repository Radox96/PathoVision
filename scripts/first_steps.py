#import required packages 
import sys, traceback
import cv2 as cv
import numpy as np 
import plantcv as pcv
import argparse
import string
import os


### Parse command-line arguments
def options():
    parser = argparse.ArgumentParser(description="Imaging processing with opencv")
    parser.add_argument("-i", "--image", help="Input image file.", required=True)
    parser.add_argument("-o", "--outdir", help="Output directory for image files.", required=False)
    parser.add_argument("-r","--result", help="result file.", required= False )
    parser.add_argument("-w","--writeimg", help="write out images.", default=False)
    parser.add_argument("-D", "--debug", help="Turn on debug, prints intermediate images.", default=None)
    args = parser.parse_args()
    return args

#import image 
import os

#check wether given img path is correct
def read_img(path):
    str -> np.ndarray
    if os.path.isfile(path):
        return cv2.imread(path)
    else:
        raise ValueError('Path provided is not a valid file: {}'.format(path))
    
    #define img-path
    path = '/github/PathoCV/test_img/test_001.JPG'
    #actual img import
    im = cv.imread(path, 1)
    #converte to grayscale
    gray_img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        #write converted img 
        cv2.imwrite('image_grey.jpg', grey_image)
        #display converted img
        cv2.imshow('greyscale', image_grey.jpg

#End of code 
