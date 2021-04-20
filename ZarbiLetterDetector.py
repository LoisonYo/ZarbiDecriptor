from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import collections

class ZarbiLetterDetector:
    """
    class ZarbiLetterDetector
    ----------
    detect all letters shape in the entry image
    """
    def process(self, img):
        """
        parameter
        ---------
        img: np.ndarray
            entry image with Zarbi translated text
        ---------
        Detect all letters in the picture, and put them in evidence with a rectangle bundary

        return the same picture with the boundary
        """
        inverse = cv2.bitwise_not(img)
        contours, hierarchy = cv2.findContours(inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        toShow = img
        toSort = dict()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            #if w*h > 100:
            toSort[x] = [x, y, w, h]
            cv2.rectangle(toShow, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cv2.imshow("detection", toShow)

        letters = []
        for key in sorted(toSort):
            x, y, w, h = toSort[key]
            letters.append(img[y:y+h, x:x+w])

        return letters