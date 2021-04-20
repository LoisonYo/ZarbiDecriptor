import os
import glob
import numpy as np
from cv2 import cv2

if __name__ == "__main__":

    zarbis = dict()
    os.chdir("./zarbis")
    for file in glob.glob("*.png"):
        img = cv2.imread(file)
        filename = file.split('.')
        zarbis[filename[0]] = img
    os.chdir("../others")

    with open("ratio.txt", "w") as writer:
        for key, value in zarbis.items():
            writer.writelines(key + "\n")
            zarbiArray = []
            for c in key:
                zarbiArray.append(zarbis[c])

            img = cv2.hconcat(zarbiArray)  

            dic = {}
            for name, template in zarbis.items():
                img_res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
                img_res = np.around(img_res, 3)

                writer.writelines("%s => %s\n" % (name, max(max(img_res))))
            writer.writelines("\n\n")    