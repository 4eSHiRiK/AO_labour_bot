import pyautogui
import time


"""
Script to find cursor coords on screen
"""

try:
    while True:
        x, y = pyautogui.position()
        print(f"Coords of cursor: X={x}, Y={y}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Script stopped.")
