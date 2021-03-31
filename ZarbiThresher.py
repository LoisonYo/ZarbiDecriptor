from cv2 import cv2
import matplotlib.pyplot as plt

class ZarbiThresher:
    def process(self, img):

        thresh = 127.5
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plt.hist(img.ravel(),256,[0,256])
        plt.show(block=False)

        ret, thresh = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

        return thresh