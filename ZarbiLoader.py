import os
import glob
from cv2 import cv2

class ZarbiLoader:
    """
    class ZarbiLoader
    load all templates stored in the app
    """
    def process(self):
        """
        method process
        iterate trought the `zarbis` folder and map characters to images
        return: a dictionnary with {'a' => a.png, ...}
        """
        zarbis = dict()

        os.chdir("./zarbis")
        for file in glob.glob("*.png"):
            img = cv2.imread(file)
            filename = file.split('.')
            zarbis[filename[0]] = img
        os.chdir("../")

        return zarbis