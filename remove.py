import pyautogui
import time

def find_setting():
    image_path = "remove.png"  # Replace with your file name

    while True:
        try:
            time.sleep(0.5)
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                # Save current mouse position before clicking
                prev_x, prev_y = pyautogui.position()

                # Click the center of the found image
                center = pyautogui.center(location)
                pyautogui.click(center)

                # Move back to the previous position
                pyautogui.moveTo(prev_x, prev_y)
            else:
                pass
        except Exception:
            pass

def find_right():
    image_path = "right.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                # Save current mouse position before clicking
                prev_x, prev_y = pyautogui.position()

                # Click the center of the found image
                center = pyautogui.center(location)
                pyautogui.click(center)

                # Move back to the previous position
                pyautogui.moveTo(prev_x, prev_y)
                break
            else:
                break
        except Exception:
            break

def find_gems():
    image_path = "gems.png"  # Replace with your file name

    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)

            if location:
                # Save current mouse position before clicking
                prev_x, prev_y = pyautogui.position()

                # Click the center of the found image
                center = pyautogui.center(location)
                pyautogui.click(center)

                # Move back to the previous position
                pyautogui.moveTo(prev_x, prev_y)
                break
            else:
                break
        except Exception:
            break

while True:
    find_right()
    find_gems()

# find_setting()