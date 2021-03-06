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

### Main pipeline
def main():
    # Get options
    args = options()

    # Read image
    img, path, test = pcv.readimage(args.image)

    debug=args.debug 

    # Pipeline step
    device = 0
    
    
    


#End of code 
