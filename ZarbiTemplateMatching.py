from cv2 import cv2
import numpy as np

class ZarbiTemplateMatching:
    """
    class ZarbiTemplateMatching
    ----------
    Match image part with templates
    """
    def process(self, letters, templates):
        """
        Parameters
        ----------
        letters:
            list

        templates: 
            dictionnary
        ----------
        Detect the letter thought the ressemblance with her template.
        
        return the string result from the detection
        """
        result = ""

        grayTemplates = dict()
        for name, zarbi in templates.items():
            grayTemplates[name] = cv2.cvtColor(zarbi, cv2.COLOR_BGR2GRAY)

        for letter in letters:
            height = letter.shape[0]
            width = letter.shape[1]
            res = dict()
            for name, zarbi in grayTemplates.items():
                zarbi = cv2.resize(zarbi, (width, height))
                res[name] = cv2.matchTemplate(letter, zarbi, cv2.TM_CCOEFF_NORMED)[0][0]
            result += max(res, key=res.get)

        return result