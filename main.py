import tkinter
from cv2 import cv2
import numpy as np
from ZarbiLoader import ZarbiLoader
from ZarbiEncryptor import ZarbiEncryptor
from ZarbiNoiseMaker import ZarbiNoiseMaker
from ZarbiThresher import ZarbiThresher
from ZarbiTemplateMatching import ZarbiTemplateMatching
from ZarbiSizeManager import ZarbiSizeManager

window = tkinter.Tk()
inputText = tkinter.Entry(window, textvariable="abcdefghijklmnopqrstuvwxyz", width=30)

def displayWindow():
    label = tkinter.Label(window, text="Texte à convertir:")
    label.pack()

    inputText.pack()

    button = tkinter.Button(window, text="Convertir", command=work)
    button.pack()

    window.mainloop()

def work():
    text = inputText.get()

    #img = ZarbiEncryptor().process(text, zarbis)
    img = cv2.imread("./img.png")

    #img = ZarbiNoiseMaker().process(img, noise_type='blur')
    cv2.imshow("default", img)

    img = ZarbiThresher().process(img)
    cv2.imshow("threshed", img)

    letters = ZarbiSizeManager().process(img)
    for i in range(len(letters)):
        cv2.imshow(str(i), letters[i])

    result = ZarbiTemplateMatching().process(letters, zarbis)

    print(result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    zarbis = ZarbiLoader().process()
    displayWindow()