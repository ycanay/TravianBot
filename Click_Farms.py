import pyautogui as pag
import random
import Detect_edge as de
import screenshot

def click_farms():
    pag.moveTo(1137, 419, random.uniform(2.0, 3.0))
    pag.click()
    pag.moveTo(1137, 474, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 517, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 638, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 680, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 740, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 790, random.uniform(0.3, 1.0))
    pag.click()
    pag.moveTo(1137, 835, random.uniform(0.3, 1.0))
    pag.click()

def go_farm_list():
    pag.moveTo(753, 111, random.uniform(1.0, 2.0))
    pag.click()
    pag.moveTo(1122, 484, random.uniform(1.0, 2.0))
    pag.click()

def open_edge():
    image = screenshot.take_screenshot()
    if de.is_edge(image):
        return
    else:
        pag.moveTo(470, 1058)
        pag.click()
