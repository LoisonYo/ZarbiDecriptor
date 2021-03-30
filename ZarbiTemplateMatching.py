from cv2 import cv2
import numpy as np

class ZarbiTemplateMatching:
    def process(self, img, templates, delta):
        dic = {}
        text_res = ""
        for name, template in templates.items():
            img_res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            img_res = np.around(img_res, 3)

            img_res = np.where(img_res >= 1 - delta)
            for x in img_res[1]:
                dic[x] = name

        for key in sorted(dic.keys()):
            text_res += dic[key]

        return text_res