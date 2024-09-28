import pyautogui
from win32gui import GetWindowText, GetForegroundWindow


pyautogui.hotkey('alt','tab')
print(GetWindowText(GetForegroundWindow()))