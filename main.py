import tkinter
import os
import glob
from cv2 import cv2
import numpy as np
from ZarbiEncryptor import ZarbiEncryptor
from ZarbiNoiseMaker import ZarbiNoiseMaker
from ZarbiTemplateMatching import ZarbiTemplateMatching
from ZarbiSizeManager import ZarbiSizeManager

window = tkinter.Tk()
inputText = tkinter.Entry(window, textvariable="abcdefghijklmnopqrstuvwxyz", width=30)

def initZarbis(zarbis):
    os.chdir("./zarbis")
    for file in glob.glob("*.png"):
        img = cv2.imread(file)
        filename = file.split('.')
        zarbis[filename[0]] = img
    os.chdir("../")

def displayWindow():
    label = tkinter.Label(window, text="Texte à convertir:")
    label.pack()

    inputText.pack()

    button = tkinter.Button(window, text="Convertir", command=work)
    button.pack()

    window.mainloop()

def work():
    #text = inputText.get().lower()
    zarbiText = cv2.imread("img.png")

    #zarbiText = ZarbiEncryptor().process(text, zarbis)
    cv2.imshow("zarbi", zarbiText)

    zarbiNoisyText = ZarbiNoiseMaker().process(zarbiText, noise_type='speckle')
    cv2.imshow("zarbi noise", zarbiNoisyText)

    #zarbiText = ZarbiSizeManager().process(zarbiText, zarbis['a'].shape[0])
    #cv2.imshow("resize", zarbiText)

    #text = ZarbiTemplateMatching().process(zarbiNoisyText, zarbis, 0.03)
    print(text)

if __name__ == "__main__":
    zarbis = dict()
    initZarbis(zarbis)
    displayWindow()