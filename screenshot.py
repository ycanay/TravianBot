import pyautogui as pag
import cv2 as cv
import numpy as np

def take_screenshot():
    image = pag.screenshot()
    image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    return image