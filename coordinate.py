import pyautogui
import time

# print("Press Ctrl+C to stop...\n")
try:
    while True:
        x, y = pyautogui.position()  # Get current mouse coordinates
        print(f"Mouse Position: X={x}, Y={y}")
        time.sleep(2)  # Delay of 1 second
except KeyboardInterrupt:
    pass
    # print("\nProgram stopped by user.")
