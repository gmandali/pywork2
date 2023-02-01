import pyautogui
import time

for i in range(3):
    pyautogui.moveTo(567, 925, 3)
    pyautogui.click(567, 925)
    time.sleep(2)
    pyautogui.moveTo(1337, 813, 3)
    pyautogui.click(1337, 813)
    time.sleep(2)
# this is the coordinates of the like button Point(x=567, y=925)
# coordinates of the next video Point(x=1337, y=813)