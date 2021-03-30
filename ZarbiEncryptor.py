from cv2 import cv2

class ZarbiEncryptor:
    def process(self, text, templates):
        zarbiArray = []
        for c in text:
            zarbiArray.append(templates[c])

        return cv2.hconcat(zarbiArray)    