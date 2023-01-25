import cv2
import numpy as np

class image:

    def OpenImage(imagepath, windowName):
        img = cv2.imread(imagepath)
        cv2.imshow(windowName, img)