from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

class ZarbiThresher:
    """
    class ZarbiThresher
    ----------
    Apply a threshold to avoir bord effect due to noise
    """
    def process(self, img):
        """
        Parameters
        ----------
        img: np.ndarray
        ----------
        Apply a binary thresh combined with an otsu one to suppress some noise

        return the threshed image
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plt.hist(gray.ravel(), 256, [0, 256])
        plt.show(block=False)

        ret, thresh = cv2.threshold(gray, 0 , 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return thresh