import pyautogui
from time import sleep


pyautogui.hotkey('alt','tab')

for i in range(12):
    pyautogui.moveTo(240,457)
    sleep(.6)
    pyautogui.click(240,457) #3 pontos
    sleep(.6)
    pyautogui.click(242,694) #delet
    sleep(.6)
    pyautogui.click(1133,602) #yes
    print(i)
    sleep(2)


# xxx =pyautogui.position()
# print(xxx)
pyautogui.hotkey('alt','tab')