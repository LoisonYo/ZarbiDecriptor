import os
import glob
from cv2 import cv2
import numpy as np

if __name__ == "__main__":
    text = "Salut".lower()

    zarbis = dict()
    os.chdir("./zarbis")
    for file in glob.glob("*.png"):
        img = cv2.imread(file)
        filename = file.split('.')
        zarbis[filename[0]] = img
    os.chdir("../")

    horizontal_margin = 5
    vertical_margin = 20
    zarbiArray = []
    
    for c in text.lower():
        zarbiArray.append(zarbis[c])

    height = max([_a.shape[0] for _a in zarbis.values()])

    for c in range(len(zarbiArray)):
        zarbi = zarbiArray[c]
        width = zarbiArray[c].shape[1] + (2 * horizontal_margin)
        offset_x = horizontal_margin
        offset_y = height - zarbi.shape[0] + vertical_margin
        image = np.ones((height + (2 * vertical_margin), width, 3), np.uint8) * 255
        image[offset_y:offset_y+zarbi.shape[0], offset_x:offset_x+zarbi.shape[1]] = zarbi
        zarbiArray[c] = image

    img = cv2.hconcat(zarbiArray)
    img = cv2.resize(img, (500, 500))
    cv2.imwrite("./img.png", img)
