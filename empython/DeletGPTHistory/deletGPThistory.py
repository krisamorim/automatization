import pyautogui
from time import sleep


pyautogui.hotkey('alt','tab')

for i in range(3):
    pyautogui.moveTo(219,457)
    sleep(.5)
    pyautogui.click(220,457) #3 pontos
    sleep(.7)
    pyautogui.click(242,614) #delet
    sleep(.7)
    pyautogui.click(1133,652) #yes
    print(i)
    sleep(2)


# xxx =pyautogui.position()
# print(xxx)
pyautogui.hotkey('alt','tab')