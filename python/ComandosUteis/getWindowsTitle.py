import pyautogui
from win32gui import GetWindowText, GetForegroundWindow


pyautogui.hotkey('alt','tab')
print('O nome da tela atual: ')
print(GetWindowText(GetForegroundWindow()))