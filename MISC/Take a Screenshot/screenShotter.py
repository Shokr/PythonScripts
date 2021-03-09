import pyautogui
import time

time.sleep(3)

img = pyautogui.screenshot()

img.save(r"image.png")
