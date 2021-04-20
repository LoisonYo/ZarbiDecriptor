from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

def getFileNameFromIndex(i):
    if i < 26:
        return chr(97 + i)
    elif i == 26:
        return '!'
    elif i == 27:
        return '?'
    else:
        return None

if __name__ == "__main__":
    img = cv2.imread('./others/base.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    letters = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        letters.append(img[y:y+h, x:x+w])
    
    for i in range(len(letters)):
        cv2.imwrite("./zarbis/%i.png" % (i), letters[i])
    