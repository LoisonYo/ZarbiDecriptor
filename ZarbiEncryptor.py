from cv2 import cv2
import numpy as np

class ZarbiEncryptor:
    def process(self, text, templates):
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