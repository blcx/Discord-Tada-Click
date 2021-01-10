import pyautogui, time , keyboard, win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def tada():
    if pyautogui.locateOnScreen('tada.png',grayscale=True, confidence=0.9) != None:

        image = pyautogui.locateOnScreen('tada.png',grayscale=True, confidence=0.9)

        x, y = pyautogui.center(image)
        pyautogui.moveTo(x, y)
        pyautogui.click()
    time.sleep(2)

Run_Times = 0
while keyboard.is_pressed('q') != True:
    tada()
    Run_Times = Run_Times + 1
    print("Run Times" + str(Run_Times))

