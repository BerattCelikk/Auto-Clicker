import pyautogui
import keyboard
import time

def clickfunc(stop_click):
    try:
        print("Move the mouse to the position and press '{}' to set the click position.".format(stop_click))
        while True:
            if keyboard.is_pressed(stop_click):
                x, y = pyautogui.position()
                print("Click position set at: ({}, {})".format(x, y))
                time.sleep(1)  
                break

        print("Auto clicker started. Press '{}' to stop.".format(stop_click))
        while True:
            pyautogui.click(x, y)
            time.sleep(1)
            if keyboard.is_pressed(stop_click):
                print("Auto clicker has stopped.")
                break

    except KeyboardInterrupt:
        print("Auto clicker has stopped.")

stop_click = 'space'

clickfunc(stop_click)
