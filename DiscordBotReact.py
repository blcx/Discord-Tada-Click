import pyautogui, time , keyboard, win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def clickicon():
    image = pyautogui.locateOnScreen('tada.png', grayscale=True, confidence=0.9)
    if image != None:
        x, y = pyautogui.center(image)
        pyautogui.moveTo(x, y)
        #pyautogui.click()


def find_airdrop_panel():
    cordinates = pyautogui.locateAllOnScreen('airdrop_panel.png',confidence=0.8)
    for element in cordinates:
        if element != None:
            tada = pyautogui.locateOnScreen('tada.png', grayscale=True, confidence=0.9,
                                            region=(element[0], element[1], element[2], element[3]))
            if tada != None:
                print("tada icon found")
                pyautogui.moveTo(tada)
                pyautogui.click()
                print("clicked")
                pyautogui.moveTo(1079/2,1919/2)




Run_Times = 0
while keyboard.is_pressed('q') != True:
    find_airdrop_panel()
    time.sleep(1)
    Run_Times = Run_Times + 1
    print("Run Times" + str(Run_Times))

