"""
Automate any Chat-Messenger with Python
Easily automate Whatsapp | Facebook | Instagram Chat-Messenger with Python using PyAutoGUI
"""
import time

import pyautogui

time.sleep(5)

text = "I Love You"

while True:
    pyautogui.typewrite(text)

    time.sleep(1)
    pyautogui.press("enter")
