import time
import pyautogui
import os
import pygetwindow as gw
import win32gui





def minimize_vscode():
    try:
        # Find all VS Code windows
        windows = [w for w in gw.getWindowsWithTitle('Visual Studio Code') if w]
        if not windows:
            print("❌ VS Code window not found.")
            return

        for win in windows:
            if not win.isMinimized:
                win.minimize()
                print(f"✅ Minimized: {win.title}")
            else:
                print(f"ℹ️ Already minimized: {win.title}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

def is_clash_open():
    windows = []

    def callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append(title)
    win32gui.EnumWindows(callback, None)

    for title in windows:
        if "clash of clans" in title.lower():
            return True
    return False

def launch_coc():
    shortcut_path = r"C:\Users\Amigo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Google Play Games\Clash of Clans.lnk"
    
    if os.path.exists(shortcut_path):
        print("🚀 Launching Clash of Clans...")
        os.startfile(shortcut_path)
        time.sleep(3)
        print("✅ Clash of Clans launched successfully!")
        minimize_vscode()
    else:
        print("❌ Shortcut not found! Please check the path.")

def find_reload():
    image_path = "Reload.png"
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                time.sleep(1)
                break
            else:
                break
        except pyautogui.ImageNotFoundException:
            break

def find_try_again():
    image_path = "TryAgain.png"
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                time.sleep(1)
                break
            else:
                find_reload()
                break
        except pyautogui.ImageNotFoundException:
            find_reload()
            break

def find_reload_game():
    image_path = "ReloadGame.png"
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                time.sleep(1)
                break
            else:
                find_try_again()
                break
        except pyautogui.ImageNotFoundException:
            find_try_again()
            break


def isGameRunning():
    if is_clash_open():
        find_try_again()
    else:
        launch_coc()

