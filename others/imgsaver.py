import os
import glob
from cv2 import cv2

if __name__ == "__main__":
    text = "Salut".lower()

    zarbis = dict()
    os.chdir("../zarbis")
    for file in glob.glob("*.png"):
        img = cv2.imread(file)
        filename = file.split('.')
        zarbis[filename[0]] = img
    os.chdir("../others")
    
    zarbiArray = []
    for c in text:
        zarbiArray.append(zarbis[c])

    img = cv2.hconcat(zarbiArray)
    cv2.imwrite("../img.png", img)
