from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import collections

class ZarbiSizeManager:
    def process(self, img):
        inverse = cv2.bitwise_not(img)
        contours, hierarchy = cv2.findContours(inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        toSort = dict()
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            toSort[x] = [x, y, w, h]

        letters = []
        for key in sorted(toSort):
            x, y, w, h = toSort[key]
            letters.append(img[y:y+h, x:x+w])

        return letters