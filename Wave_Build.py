import pyautogui as pag
import random
import Click_Farms as cf

def send_waves(no_wave = 7):
    click_place = 1180
    cf.open_edge()
    pag.moveTo(click_place, 590, 0.2)
    pag.click()
    for i in range(no_wave-1):
        pag.hotkey('ctrl', 'tab')
        click_place += 1
        pag.moveTo(click_place, 590, 0.1)
        pag.click()

send_waves(7)