import time
import numpy as np
import pyautogui
import sys
import os
import gc
import logging
import re
from PIL import ImageGrab
from paddleocr import PaddleOCR


# 🔇 1. Silence Paddle’s internal C++ logs
os.environ["FLAGS_logging_level"] = "3"   # 0=ALL, 1=WARN, 2=ERROR, 3=FATAL
os.environ["GLOG_minloglevel"] = "3"      # Hide INFO/DEBUG/WARN from GLOG

# 🔇 2. Silence Python ppocr logger
logging.getLogger("ppocr").setLevel(logging.ERROR)

# 🔇 3. Redirect stderr (Paddle prints logs there)
sys.stderr = open(os.devnull, "w")

# Initialize PaddleOCR once (better than reloading each call)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def change_account():
    image_path1 = "setting.png"
    image_path2 = "changeaccount.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path1, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.moveTo(center)
                pyautogui.click()
                time.sleep(.5)

                location = pyautogui.locateOnScreen(image_path2, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    pyautogui.click(center)
                    break
                else:
                    pass

            else:
                pass
        except Exception as e:
            pass

def defenceRun():
    pyautogui.click(100,971)
    pyautogui.moveTo(360,33)
    pyautogui.mouseDown()
    pyautogui.moveTo(600,33)
    pyautogui.mouseUp()

def find_settingforverification():
    image_path = "setting.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                clearNotice()
                find_claim()
                break
            else:
                defenceRun()
                pass
        except pyautogui.ImageNotFoundException:
            defenceRun()
            pass

def find_claim():
    image_path = "claim.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                break
            else:
                break
        except Exception as e:
            break

def find_black():
    image_path = "blackscreen.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                pass
            else:
                find_settingforverification()
                break
        except Exception as e:
            find_settingforverification()
            break

def find_supercellfordonation():
    image_path = "supercell.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.moveTo(center)
                break
            else:
                pass
        except Exception as e:
            pass

def clearNotice():
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,44)
    time.sleep(1)
    pyautogui.click(1857,400)

def scroll_up():
    pyautogui.moveTo(1643,1031)
    pyautogui.mouseDown()
    pyautogui.moveTo(1643,390,.5)
    pyautogui.mouseUp()

def find_clans():
    image_path = "Clans.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location.left+30,location.top+20)
                find_search_clans()
                break
            else:
                pass
        except Exception as e:
            pass

def find_search_clans():
    image_path = "searchClans.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                break
            else:
                pass
        except Exception as e:
            pass

def find_search_button():
    image_path = "searchButton.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(607,345)
                time.sleep(1)
                pyautogui.write("#2YGY98UJP")
                time.sleep(.5)
                pyautogui.click(location)
                break
            else:
                pass
        except Exception as e:
            pass

def find_clan_name():
    image_path = "whiteDevil.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                find_join_button()
                break
            else:
                pass
        except Exception as e:
            pass

def find_join_button():
    image_path = "joinButton.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                find_okay_button()
                break
            else:   
                pass
        except Exception as e:
            pass

def find_okay_button():
    image_path = "okayButton.png"

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                break
            else:   
                pass
        except Exception as e:
            pass

def join_whiteDevil():
    pyautogui.click(58,48)
    find_clans()
    find_search_button()
    find_clan_name()

def mainJoinRun():

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+07
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+06
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+05
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+04
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+03
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+02
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu+01
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu07
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu06
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu05
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,1042) # Buggu04
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,891) # Buggu03
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,755) # Buggu02
    find_supercellfordonation()
    find_black()
    join_whiteDevil()
    
    change_account()
    time.sleep(1)
    pyautogui.click(1653,609) # Buggu01
    find_supercellfordonation()
    find_black()
    join_whiteDevil()

mainJoinRun()

