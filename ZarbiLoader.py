import os
import glob
from cv2 import cv2

class ZarbiLoader:
    def process(self):
        zarbis = dict()

        os.chdir("./zarbis")
        for file in glob.glob("*.png"):
            img = cv2.imread(file)
            filename = file.split('.')
            zarbis[filename[0]] = img
        os.chdir("../")

        return zarbis