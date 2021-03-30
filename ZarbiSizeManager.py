from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

class ZarbiSizeManager:
    def process(self, img, letterSize):
        if img.shape[0] == letterSize:
            return img

        thresh = 250
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        average = np.around(gray.mean(axis=0))
        threshold = [255 if a_ > thresh else 0 for a_ in average]

        plt.figure(1)
        plt.subplot(211)
        plt.plot(average)
        plt.subplot(212)
        plt.plot(threshold)
        #plt.show()

        diff = np.diff(threshold)
        old_x = 0
        letters = []
        for i in range(0, len(diff)):
            if diff[i] < 0:
                old_x = i
            elif diff[i] > 0:
                letters.append(img[0:img.shape[0], old_x:i])

        for i in range(len(letters)):
            cv2.imshow(str(i), letters[i])

        dim = (img.shape[1], letterSize)
        return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)