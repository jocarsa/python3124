# pip install PyAutoGUI
import pyautogui as auto
import time

auto.moveTo(1222,397)
time.sleep(2)
auto.click()
time.sleep(2)
auto.write("Este es un texto que estoy escribiendo desde Python",interval=0.1)
auto.press('enter')
auto.write("Este es otro  texto que estoy escribiendo desde Python",interval=0.1)
auto.press('enter')
