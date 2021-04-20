from cv2 import cv2
import numpy as np

class ZarbiEncryptor:
    """
    class ZarbiNoiseEncryptor
    Generate a zarbi text from string text
    """
    def process(self, text, templates):
        """
        method process
        parameters
        ----------
        text: string
            the text string that will be encoded
        templates: array
            an array of image template that will be the result image
        ----------
        iterate trought an array of templates to create an image from an entry string, for exemple, the string `hello`
        will create an `hello` translation in zarbi
        return:
            The translated image
        """
        horizontal_margin = 5
        vertical_margin = 20
        zarbiArray = []
        
        for c in text.lower():
            zarbiArray.append(templates[c])

        height = max([_a.shape[0] for _a in templates.values()])

        for c in range(len(zarbiArray)):
            zarbi = zarbiArray[c]
            width = zarbiArray[c].shape[1] + (2 * horizontal_margin)
            offset_x = horizontal_margin
            offset_y = height - zarbi.shape[0] + vertical_margin
            image = np.ones((height + (2 * vertical_margin), width, 3), np.uint8) * 255
            image[offset_y:offset_y+zarbi.shape[0], offset_x:offset_x+zarbi.shape[1]] = zarbi
            zarbiArray[c] = image

        return cv2.hconcat(zarbiArray)    