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



# Loot Code Started

def extract_data(x, y, width, height):
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

def attack_Button():
    attack1_img = "attack1.png"   # first attack button

    while True:
        try:
            location = pyautogui.locateOnScreen(attack1_img, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                time.sleep(.5)
                attack_Button2()
            else:
                break
        except Exception as e:
            break

def attack_Button2():
    attack2_img = "attack2.png"   # second attack button

    while True:
        try:
            location = pyautogui.locateOnScreen(attack2_img, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                time.sleep(.5)
                break
            else:
                break
        except Exception as e:
            break

def find_next():
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

def find_returnHome():
    print("Returning Home...")
    image_path = "returnHome.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                pyautogui.click()
                pyautogui.click()
                find_setting()
                break
            else:
                pass
        except Exception as e:
            pass

def zoom_out():
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

    pyautogui.click(97-x,279-y)
    pyautogui.click(864-x,856-y)
    pyautogui.click(1647-x,280-y)

    pyautogui.click(97,279)
    pyautogui.click(864,856)
    pyautogui.click(1647,280)

    pyautogui.click(97+x,279+y)
    pyautogui.click(864+x,856+y)
    pyautogui.click(1647+x,280+y)

def deploy_ed(x=15,y=15):
    pyautogui.click(332,994) #Select Ed

    pyautogui.click(373-x,63-y)
    pyautogui.click(97-x,279-y)
    pyautogui.click(294-x,438-y)
    pyautogui.click(485-x,578-y)
    pyautogui.click(685-x,725-y)
    pyautogui.click(864-x,856-y)
    pyautogui.click(1078-x,708-y)
    pyautogui.click(1274-x,558-y)
    pyautogui.click(1487-x,403-y)
    pyautogui.click(1647-x,280-y)
    pyautogui.click(1357-x,42-y)

    pyautogui.click(373,63)
    pyautogui.click(97,279)
    pyautogui.click(294,438)
    pyautogui.click(485,578)
    pyautogui.click(685,725)
    pyautogui.click(864,856)
    pyautogui.click(1078,708)
    pyautogui.click(1274,558)
    pyautogui.click(1487,403)
    pyautogui.click(1647,280)
    pyautogui.click(1357,42)

    pyautogui.click(373+x,63+y)
    pyautogui.click(97+x,279+y)
    pyautogui.click(294+x,438+y)
    pyautogui.click(485+x,578+y)
    pyautogui.click(685+x,725+y)
    pyautogui.click(864+x,856+y)
    pyautogui.click(1078+x,708+y)
    pyautogui.click(1274+x,558+y)
    pyautogui.click(1487+x,403+y)
    pyautogui.click(1647+x,280+y)
    pyautogui.click(1357+x,42+y)

def deploy_hero(x=15,y=15):
    pyautogui.click(594,994) #King
    pyautogui.click(373-x,63-y)
    pyautogui.click(373,63)
    pyautogui.click(373+x,63+y)

    pyautogui.click(714,987) #Queen
    pyautogui.click(485+x,578-y)
    pyautogui.click(485,578)
    pyautogui.click(485-x,578+y)

    pyautogui.click(836,994) #Warden
    pyautogui.click(1274-x,578-y)
    pyautogui.click(1274,578)
    pyautogui.click(1274+x,578+y)

    pyautogui.click(958,991) #Queen
    pyautogui.click(1357-x,42+y)
    pyautogui.click(1357,42)
    pyautogui.click(1357+x,42-y)

def deploy_cc(x=15,y=15):
    pyautogui.click(466,994)
    pyautogui.click(373-x,63-y)
    pyautogui.click(373,63)
    pyautogui.click(373+x,63+y)

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

def Looting():
    zoom_out()
    attack_Button()
    while True:
        find_next()
        time.sleep(1)
        exlier_enemy=extract_data(76,167,200,35)
        if exlier_enemy>=loot_elixer_threshold:
            print(f"Loot {exlier_enemy} Found Attacking...")
            zoom_out()
            zoom_out()
            swipe_up()
            swipe_up()
            deployTroop()
            find_returnHome()
            break
        else:
            pyautogui.click(1781,795)
            pyautogui.click(1781,795)
            time.sleep(1)

# Loot Code Ended



#Request Troop Code Start

def find_donateButton():
    image_path = "donateButton.png"  # Replace with your file name

    print("✅ Donation Started...")
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
            print("✅ Donation Stopped...")
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


def find_settingforDonation():
    image_path = "setting.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                center = pyautogui.center(location)
                pyautogui.moveTo(center)
                find_claim()
                break
            else:
                defenceRun()
        except Exception as e:
            defenceRun()

def find_setting():
    image_path = "setting.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                break
            else:
                pass
        except Exception as e:
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
    clearNotice()
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

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(9): # Buggu+30
        scroll_up()
    pyautogui.click(1653,761)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(8): # Buggu+29
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(8): # Buggu+28
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(8): # Buggu+27
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(8): # Buggu+26
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(7): # Buggu+25
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(7): # Buggu+24
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(7): # Buggu+23
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(7): # Buggu+22
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(6): # Buggu+21
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(6): # Buggu+20
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(6): # Buggu+19
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(6): # Buggu+18
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(5): # Buggu+17
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(5): # Buggu+16
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(5): # Buggu+15
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(5): # Buggu+14
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(4): # Buggu+13
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(4): # Buggu+12
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(4): # Buggu+11
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(4): # Buggu+10
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(3): # Buggu+09
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(3): # Buggu+08
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(3): # Buggu+07
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(3): # Buggu+06
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(2): # Buggu+05
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(2): # Buggu+04
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(2): # Buggu+03
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(2): # Buggu+02
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(1): # Buggu+01
        scroll_up()
    pyautogui.click(1653,1042)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(1): # Buggu07
        scroll_up()
    pyautogui.click(1653,891)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(1): # Buggu06
        scroll_up()
    pyautogui.click(1653,755)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    for _ in range(1): # Buggu05
        scroll_up()
    pyautogui.click(1653,609)
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    pyautogui.click(1653,1042) # Buggu04
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    pyautogui.click(1653,891) # Buggu03
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()

    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    pyautogui.click(1653,755) # Buggu02
    find_supercellfordonation()
    find_settingforDonation()
    request_troop()
    
    find_settingforDonation()
    pyautogui.click()
    time.sleep(.5)
    pyautogui.click(1236,225)
    time.sleep(1)
    pyautogui.click(1653,609) # Buggu01
    find_supercellfordonation()
    find_settingforDonation()
    print("Troop Request Ended")

def defenceRun():
    pyautogui.click(100,971)
    pyautogui.moveTo(360,33)
    pyautogui.mouseDown()
    pyautogui.moveTo(600,33)
    pyautogui.mouseUp()

def ReqAndDonate():
    mainReqRun()
    clearNotice()
    donateTroop()

#Request Troop Code End


def trophyDecrease():
    zoom_out()
    while True:
        trophy = extract_data(110, 137, 110, 32)

        if trophy > min_trophy:
            print(f"{trophy} > {min_trophy}, start decreasing trophies")
            for _ in range(10):  # ✅ correct loop
                attack_Button()
                find_next()
                pyautogui.click(332,994)
                pyautogui.click(1754+15, 530)
                pyautogui.click(1754, 530)
                pyautogui.click(1754-15, 530)
                pyautogui.click(117, 851)
                pyautogui.click(1106, 666)
                find_returnHome()
                time.sleep(.5)
        else:
            print(f"{trophy} < {min_trophy}, no need to decrease trophies")
            break

def trophyDecreasefordonate():
    for _ in range(5):
        zoom_out()
        attack_Button()
        find_next()
        pyautogui.click(332,994)
        pyautogui.click(1754+15, 530)
        pyautogui.click(1754, 530)
        pyautogui.click(1754-15, 530)
        pyautogui.click(117, 851)
        pyautogui.click(1106, 666)
        find_returnHome()

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



home_elixer_threshold=28000000
donate_threshold=25000000
loot_elixer_threshold=200000
min_trophy=400


while True:
    donateTroop()
    try:
        clearNotice()
        home_elixer = extract_data(1594, 117, 250, 35)

        if home_elixer >= donate_threshold:
            print(f"[DONATE] {home_elixer} ≥ {donate_threshold} → Donating...")
            ReqAndDonate()

        else:
            # trophyDecrease()

            while True:
                time.sleep(1)
                home_elixer1 = extract_data(1594, 117, 250, 35)
                print(f"[LOOTING] {home_elixer1} < {donate_threshold} → Start Looting...")

                if home_elixer1 <= home_elixer_threshold:
                    Looting()
                else:
                    print(f"[STOP LOOTING] {home_elixer1} ≥ {home_elixer_threshold} → Back to donation check")
                    break

    except Exception as e:
        print(f"[ERROR] {e} → Restarting loop from start...")
        continue   # go back to start of outer while True





