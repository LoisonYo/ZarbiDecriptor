import tkinter
from cv2 import cv2
import numpy as np
from ZarbiLoader import ZarbiLoader
from ZarbiEncryptor import ZarbiEncryptor
from ZarbiNoiseMaker import ZarbiNoiseMaker
from ZarbiThresher import ZarbiThresher
from ZarbiTemplateMatching import ZarbiTemplateMatching
from ZarbiLetterDetector import ZarbiLetterDetector

window = tkinter.Tk()
inputText = tkinter.Entry(window, textvariable="abcdefghijklmnopqrstuvwxyz", width=30)
filenamefield = tkinter.Label(window)
resultField = tkinter.Label(window)

def displayWindow():
    tkinter.Label(window, text="Utilisation d'un text :").pack()
    inputText.pack()
    button = tkinter.Button(window, text="Convertir le text", command=workText)
    button.pack()

    tkinter.Label(window).pack()

    tkinter.Label(window, text="Utilisation d'une image :").pack()
    button = tkinter.Button(window, text="Charger une image", command=selectFile)
    button.pack()
    filenamefield.pack()
    button = tkinter.Button(window, text="Utiliser image", command=workFile)
    button.pack()

    tkinter.Label(window).pack()

    tkinter.Label(window, text="Résultat :").pack()
    resultField.pack()

    window.mainloop()

def selectFile():
    filename = tkinter.filedialog.askopenfilename(initialdir = "./images", title = "Select a File")
    filenamefield.config(text=filename)

def workText():
    img = ZarbiEncryptor().process(inputText.get(), zarbis)
    work(img)

def workFile():
    img = cv2.imread(filenamefield['text'])
    work(img)

def work(img):
    #cv2.imshow("default", img)

    img = ZarbiNoiseMaker().process(img, noise_type='blur')
    #cv2.imshow("poisson blur", img)

    img = ZarbiThresher().process(img)
    #cv2.imshow("threshed", img)

    kernel = np.ones((5,5),np.uint8)
    img = cv2.dilate(img, kernel, iterations = 1) #sens opencv
    img = cv2.erode(img, kernel, iterations = 1)
    #cv2.imshow("erode", img)

    letters = ZarbiLetterDetector().process(img)
    #for i in range(len(letters)):
    #    cv2.imshow(str(i), letters[i])

    result = ZarbiTemplateMatching().process(letters, zarbis)
    resultField.config(text=result)

if __name__ == "__main__":
    zarbis = ZarbiLoader().process()
    displayWindow()