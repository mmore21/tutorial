# Tic Tac Toe Player
# https://www.coolmathgames.com/0-tic-tac-toe
import pyautogui
import time

horizontal = [700, 840, 980]
vertical = [425, 560, 700]

try:
    while True:
        time.sleep(1)
        pyautogui.click(horizontal[1], vertical[0])
        time.sleep(0.5)
        pyautogui.click(horizontal[2], vertical[2])
        time.sleep(0.5)
        pyautogui.click(horizontal[1], vertical[1])
        time.sleep(0.5)
        pyautogui.click(horizontal[2], vertical[1])
        time.sleep(0.5)
        pyautogui.click(horizontal[1], vertical[2])
        time.sleep(3)
        pyautogui.click()
except KeyboardInterrupt:
    print('\nDone.')