from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

class ZarbiThresher:
    def process(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plt.hist(gray.ravel(), 256, [0, 256])
        plt.show(block=False)

        ret, thresh = cv2.threshold(gray, 0 , 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return thresh