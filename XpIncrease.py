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




def find_donateButton():
    image_path = "donateButton.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                time.sleep(0.5)  # small delay before searching again
                find_supWizard()
                time.sleep(0.5)  # small delay before searching again
            else:
                break   # stop when not found even once
        except Exception as e:
            break

def find_supWizard():
    image_path = "supWizard.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                find_loon()
                break
            else:
                donate_omi()
                break
        except pyautogui.ImageNotFoundException:
            donate_omi()
            break

def find_loon():
    image_path = "loon.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                find_lightning()
                break
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def find_loonforStone():
    image_path = "loon.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                x, y = location.left, location.top + 30
                pyautogui.moveTo(x, y)
                pyautogui.mouseDown()
                pyautogui.moveTo(5, y)
                pyautogui.mouseUp()
                time.sleep(.7)
                find_stone()
                break
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def find_lightning():
    image_path = "lightning.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                time.sleep(.3)
                find_loonforStone()
                break
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def find_stone():
    image_path = "stoneSlammer.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click(center)
                pyautogui.click(center)
                break
            else:
                break
        except pyautogui.ImageNotFoundException:
            print("not found Stone Slammer")
            break

def donateTroop():
    pyautogui.click(62,486)
    time.sleep(.5)
    find_donateButton()
    pyautogui.click(655,486)

def donate_omi():
    image_path = "resource.png"  # Replace with your file name

    while True:
        try:
            time.sleep(.5)
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.click(center.x-411,center.y+507)
                pyautogui.click(center.x-411,center.y+507)
                pyautogui.click(center.x-411,center.y+507)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+304)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(center.x-411,center.y+158)
                pyautogui.click(1857,400)

                break
            else:
                break
        except Exception as e:
            break

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
                pass
        except pyautogui.ImageNotFoundException:
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

def find_reqbtn():
    image_path = "reqBtn.png"  # Replace with your file name

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

def find_okaybtn():
    image_path = "okaybtn.png"  # Replace with your file name

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

def scroll_up():
    pyautogui.moveTo(1643,1031)
    pyautogui.mouseDown()
    pyautogui.moveTo(1643,390,.5)
    pyautogui.mouseUp()

def request_troop():
    pyautogui.click(61,826)
    time.sleep(.5)
    pyautogui.click(1412,775)
    time.sleep(.5)
    find_okaybtn()
    find_reqbtn()
    pyautogui.click(1107,710)
    pyautogui.click(1762,141)

def mainReqRun():
    print("Troop Request Started")

    change_account()
    time.sleep(1)
    for _ in range(9): # Buggu+30
        scroll_up()
    pyautogui.click(1653,761)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(8): # Buggu+29
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(8): # Buggu+28
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(8): # Buggu+27
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(8): # Buggu+26
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(7): # Buggu+25
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(7): # Buggu+24
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(7): # Buggu+23
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(7): # Buggu+22
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(6): # Buggu+21
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(6): # Buggu+20
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(6): # Buggu+19
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(6): # Buggu+18
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(5): # Buggu+17
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(5): # Buggu+16
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(5): # Buggu+15
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(5): # Buggu+14
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(4): # Buggu+13
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(4): # Buggu+12
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(4): # Buggu+11
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(4): # Buggu+10
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+09
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+08
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+07
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(3): # Buggu+06
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+05
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+04
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+03
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(2): # Buggu+02
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu+01
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu07
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu06
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    for _ in range(1): # Buggu05
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,1042) # Buggu04
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,891) # Buggu03
    find_supercellfordonation()
    find_black()
    request_troop()

    change_account()
    time.sleep(1)
    pyautogui.click(1653,755) # Buggu02
    find_supercellfordonation()
    find_black()
    request_troop()
    
    change_account()
    time.sleep(1)
    pyautogui.click(1653,609) # Buggu01
    find_supercellfordonation()
    find_black()
    print("Troop Request Ended")

def defenceRun():
    pyautogui.click(100,971)
    pyautogui.moveTo(360,33)
    pyautogui.mouseDown()
    pyautogui.moveTo(600,33)
    pyautogui.mouseUp()

def ReqAndDonate():
    mainReqRun()
    donateTroop()

def home_elixerd_data_for_donate(x, y, width, height):
    # Define bounding box
    left = x
    top = y
    right = x + width
    bottom = y + height
    
    # Take screenshot
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # screenshot.save('data.png')

    # Convert to NumPy array for PaddleOCR
    img = np.array(screenshot)
    
    # Run OCR
    results = ocr.ocr(img, cls=True)
    
    # Extract text
    text = ''
    if results and results[0]:
        for line in results[0]:
            text += line[1][0]
    
    # Keep only numbers
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    
    # Convert to integer (default 0 if empty)
    result_int = int(result) if result.isdigit() else 0
    
    # Clean up memory
    del results, screenshot
    gc.collect()
    
    return result_int

    
# Donation Code End


# Loot Code Started

def enemy_elixer_for_loot(x, y, width, height):
    # Define bounding box
    left = x
    top = y
    right = x + width
    bottom = y + height
    
    # Take screenshot
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # screenshot.save('data.png')

    # Convert to NumPy array for PaddleOCR
    img = np.array(screenshot)
    
    # Run OCR
    results = ocr.ocr(img, cls=True)
    
    # Extract text
    text = ''
    if results and results[0]:
        for line in results[0]:
            text += line[1][0]
    
    # Keep only numbers
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    
    # Convert to integer (default 0 if empty)
    result_int = int(result) if result.isdigit() else 0
    
    # Clean up memory
    del results, screenshot
    gc.collect()
    
    return result_int

def home_elixerd_data_for_loot(x, y, width, height):
    # Define bounding box
    left = x
    top = y
    right = x + width
    bottom = y + height
    
    # Take screenshot
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    # screenshot.save('data.png')

    # Convert to NumPy array for PaddleOCR
    img = np.array(screenshot)
    
    # Run OCR
    results = ocr.ocr(img, cls=True)
    
    # Extract text
    text = ''
    if results and results[0]:
        for line in results[0]:
            text += line[1][0]
    
    # Keep only numbers
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    
    # Convert to integer (default 0 if empty)
    result_int = int(result) if result.isdigit() else 0
    
    # Clean up memory
    del results, screenshot
    gc.collect()
    
    return result_int

def attack_Button_for_looting():
    attack1_img = "attack1.png"
    attack2_img = "attack2.png"

    while True:
        try:
            # --- Search Attack1 ---
            location1 = pyautogui.locateOnScreen(attack1_img, confidence=0.8)
            if not location1:
                break

            # Click Attack1
            center1 = pyautogui.center(location1)
            pyautogui.click(center1)
            time.sleep(0.5)

            # --- Search Attack2 ---
            location2 = pyautogui.locateOnScreen(attack2_img, confidence=0.8)
            if location2:
                center2 = pyautogui.center(location2)
                pyautogui.click(center2)
                time.sleep(0.5)

            # Loop continues, goes back to search for Attack1 again

        except Exception as e:
            break

def find_next_for_loot():
    image_path = "next.png"  # Replace with your file name

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

def zoom_out_for_loot():
    for _ in range(10):
        pyautogui.moveTo(1920/2,1080/2)
        pyautogui.scroll(-500)

def swipe_up():
    pyautogui.moveTo(1580,860)
    pyautogui.mouseDown()
    pyautogui.moveTo(100,50)
    pyautogui.mouseUp()

def deploy_spell(x=15,y=15):
    pyautogui.click(1101,994) #Select Clone

    pyautogui.click(240-x,525-y)
    pyautogui.click(913-x,10-y)
    pyautogui.click(1708-x,520-y)

    pyautogui.click(240,525)
    pyautogui.click(913,10)
    pyautogui.click(1708,520)

    pyautogui.click(240+x,525+y)
    pyautogui.click(913+x,10+y)
    pyautogui.click(1708+x,520+y)

def deploy_ed(x=15,y=15):
    pyautogui.click(332,994) #Select Ed

    pyautogui.click(683-x,876-y)
    pyautogui.click(491-x,714-y)
    pyautogui.click(240-x,525-y)
    pyautogui.click(515-x,312-y)
    pyautogui.click(751-x,137-y)
    pyautogui.click(913-x,10-y)
    pyautogui.click(1177-x,125-y)
    pyautogui.click(1438-x,306-y)
    pyautogui.click(1708-x,520-y)
    pyautogui.click(1539-x,675-y)
    pyautogui.click(1298-x,848-y)
    
    pyautogui.click(683,876)
    pyautogui.click(491,714)
    pyautogui.click(240,525)
    pyautogui.click(515,312)
    pyautogui.click(751,137)
    pyautogui.click(913,10)
    pyautogui.click(1177,125)
    pyautogui.click(1438,306)
    pyautogui.click(1708,520)
    pyautogui.click(1539,675)
    pyautogui.click(1298,848)
    
    pyautogui.click(683+x,8766+y)
    pyautogui.click(491+x,7146+y)
    pyautogui.click(240+x,5256+y)
    pyautogui.click(515+x,3126+y)
    pyautogui.click(751+x,1376+y)
    pyautogui.click(913+x,106+y)
    pyautogui.click(1177+x,1256+y)
    pyautogui.click(1438+x,3066+y)
    pyautogui.click(1708+x,5206+y)
    pyautogui.click(1539+x,6756+y)
    pyautogui.click(1298+x,8486+y)

def deploy_hero(x=15,y=15):
    pyautogui.click(594,994) #King
    pyautogui.click(491+x,714-y)
    pyautogui.click(491,714)
    pyautogui.click(491-x,714+y)

    pyautogui.click(714,987) #Queen
    pyautogui.click(751-x,137-y)
    pyautogui.click(751,137)
    pyautogui.click(751+x,137+y)

    pyautogui.click(836,994) #Warden
    pyautogui.click(1438+x,306-y)
    pyautogui.click(1438,306)
    pyautogui.click(1438-x,306+y)

    pyautogui.click(958,991) #Queen
    pyautogui.click(1298-x,848-y)
    pyautogui.click(1298,848)
    pyautogui.click(1298+x,848+y)

def deploy_cc(x=15,y=15):
    pyautogui.click(466,994)
    pyautogui.click(751-x,137-y)
    pyautogui.click(751,137)
    pyautogui.click(751+x,137+y)

def deployTroop():
    deploy_spell()
    deploy_ed()
    deploy_hero()
    deploy_cc()

def clearNotice():
    pyautogui.click(1857,44)
    pyautogui.click(1857,44)
    pyautogui.click(1857,44)
    pyautogui.click(1857,44)
    pyautogui.click(1857,44)
    pyautogui.click(1857,44)
    pyautogui.click(1857,400)

def find_returnHome_for_loot():
    image_path = "returnHome.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click()
                result=find_setting_for_loot()
                if result:
                    break
                else:
                    pass
            else:
                result=find_setting_for_loot()
                if result:
                    break
        except Exception as e:
                result=find_setting_for_loot()
                if result:
                    break

def find_setting_for_loot():
    image_path = "setting.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                return True
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def loot_loop():
    while True:
        home_exlier=home_elixerd_data_for_loot(1594, 117, 250, 35)
        if home_exlier>=home_elixer_threshold:
            print(f"Storage Full No Looting {home_exlier} > {home_elixer_threshold}")
            break
        else:
            print(f"Storage Empty Need Loot {home_exlier} < {home_elixer_threshold}")
            zoom_out_for_loot()
            zoom_out_for_loot()
            attack_Button_for_looting()
            while True:
                find_next_for_loot()
                time.sleep(1)
                enemy_elixer=enemy_elixer_for_loot(76,167,200,35)
                if enemy_elixer>=loot_elixer_threshold:
                    print(f"Loot {enemy_elixer} Found Attacking...")
                    deployTroop()
                    find_returnHome_for_loot()
                    time.sleep(1)
                    break
                else:
                    pyautogui.click(1781,795)
                    pyautogui.click(1781,795)
                    time.sleep(1)
                    pass



def get_trophy_for_trophy_decrease(x, y, width, height):
    # Define bounding box
    left = x
    top = y
    right = x + width
    bottom = y + height
    
    # Take screenshot
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Convert to NumPy array for PaddleOCR
    img = np.array(screenshot)
    
    # Run OCR
    results = ocr.ocr(img, cls=True)
    
    # Extract text
    text = ''
    if results and results[0]:
        for line in results[0]:
            text += line[1][0]
    
    # Keep only numbers
    numbers = re.findall(r'\d+', text)
    result = ''.join(numbers)
    
    # Convert to integer (default 0 if empty)
    result_int = int(result) if result.isdigit() else 0
    
    # Clean up memory
    del results, screenshot
    gc.collect()
    
    return result_int

def zoom_out_for_trophy_decrease():
    for _ in range(10):
        pyautogui.moveTo(1920/2,1080/2)
        pyautogui.scroll(-500)

def attack_Button_for_trophy_decrease():
    attack1_img = "attack1.png"
    attack2_img = "attack2.png"

    while True:
        try:
            # --- Search Attack1 ---
            location1 = pyautogui.locateOnScreen(attack1_img, confidence=0.8)
            if not location1:
                break

            # Click Attack1
            center1 = pyautogui.center(location1)
            pyautogui.click(center1)
            time.sleep(0.5)

            # --- Search Attack2 ---
            location2 = pyautogui.locateOnScreen(attack2_img, confidence=0.8)
            if location2:
                center2 = pyautogui.center(location2)
                pyautogui.click(center2)
                time.sleep(0.5)

            # Loop continues, goes back to search for Attack1 again

        except Exception as e:
            break

def find_next_for_trophy_decrease():
    image_path = "next.png"  # Replace with your file name

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

def find_returnHome_for_trophy_decrease():
    image_path = "returnHome.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click()
                pyautogui.click()
                result=find_setting_for_trophy_decrease()
                if result:
                    break
                else:
                    pass
            else:
                result=find_setting_for_trophy_decrease()
                if result:
                    break
        except Exception as e:
                result=find_setting_for_trophy_decrease()
                if result:
                    break

def find_setting_for_trophy_decrease():
    image_path = "setting.png"  # Replace with your file name
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                return True
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def trophyDecrease():
    zoom_out_for_trophy_decrease()
    while True:
        trophy = get_trophy_for_trophy_decrease(110, 137, 110, 32)

        if trophy > min_trophy:
            print(f"{trophy} > {min_trophy}, start decreasing trophies")
            for _ in range(10):
                attack_Button_for_trophy_decrease()
                find_next_for_trophy_decrease()
                pyautogui.click(332,994)
                pyautogui.click(1754+15, 530)
                pyautogui.click(1754, 530)
                pyautogui.click(1754-15, 530)
                pyautogui.click(117, 851)
                pyautogui.click(1106, 666)
                find_returnHome_for_trophy_decrease()
                time.sleep(.5)
        else:
            print(f"{trophy} < {min_trophy}, no need to decrease trophies")
            break

def change_account_after_error():
    image_path1 = "setting.png"
    image_path2 = "changeaccount.png"

    pyautogui.click("space")
    pyautogui.click("space")
    pyautogui.click("space")
    pyautogui.click("space")

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
                    time.sleep(1)
                    pyautogui.click(1653,609)
                    find_supercellfordonation()
                    find_black()
                    break
                else:
                    pass
            else:
                pass
        except Exception as e:
            pass

home_elixer_threshold=28000000
donate_threshold=1000000
loot_elixer_threshold=1200000
min_trophy=400

def main_loop():
    donateTroop()
    while True:
        status = home_elixerd_data_for_donate(1594, 117, 250, 35)
        if status > donate_threshold:
            print("Elixer fullfill Requirement, Donation Started")
            ReqAndDonate()
        else:
            print("Elixer Not fullfill Requirement, Loot Started")
            trophyDecrease()
            loot_loop()

while True:
    try:
        main_loop()
    except Exception as e:
        print(f"[ERROR] → Restarting app...")
        time.sleep(2)
        # Restart the script itself
        os.execv(sys.executable, ['python'] + sys.argv)
        change_account_after_error()




