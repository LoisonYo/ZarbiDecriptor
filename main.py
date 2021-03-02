import tkinter
import os
import glob
from cv2 import cv2
import numpy as np

window = tkinter.Tk()
inputText = tkinter.Entry(window, textvariable=str, width=30)

def initZarbis(zarbis):
    os.chdir("./zarbis")
    for file in glob.glob("*.png"):
        img = cv2.imread(file)
        filename = file.split('.')
        zarbis[filename[0]] = img

def displayWindow() :
    label = tkinter.Label(window, text="Texte à convertir:")
    label.pack()

    inputText.pack()

    button = tkinter.Button(window, text="Convertir", command=work)
    button.pack()

    window.mainloop()

def work() :
    text = inputText.get().lower()

    zarbiText = convert(text)
    cv2.imshow("zarbi", zarbiText)

    text = process(zarbiText)
    print(text)

def convert(text) :
    zarbiArray = []
    for c in text:
        zarbiArray.append(zarbis[c])

    return cv2.hconcat(zarbiArray)

def process(img) :
    #TODO traitement
    return "TEXT"

if __name__ == "__main__":
    zarbis = dict()
    initZarbis(zarbis)
    displayWindow()