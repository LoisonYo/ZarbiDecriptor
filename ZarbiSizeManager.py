from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
import collections

class ZarbiSizeManager:
    def process(self, img):
        inverse = cv2.bitwise_not(img)
        contours, hierarchy = cv2.findContours(inverse, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        toShow = img
        toSort = dict()

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            if w*h > 100:
                toSort[x] = [x, y, w, h]


        median = np.mean(list(map(lambda a : a[2] * a[3], toSort.values())))
        minimum = median - (median / 2)
        maximum = median + (median / 2)

        tmp = dict()
        for key, value in toSort.items():
            x, y, w, h = value
            if w*h > minimum and w*h < maximum:
                tmp[key] = value
                cv2.rectangle(toShow, (x, y), (x+w, y+h), (0, 0, 255), 3)
        toSort = tmp
        cv2.imshow("detection", toShow)

        letters = []
        for key in sorted(toSort):
            x, y, w, h = toSort[key]
            letters.append(img[y:y+h, x:x+w])

        return letters