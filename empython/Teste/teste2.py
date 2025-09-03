import pyautogui
from time import sleep
pyautogui.FAILSAFE= False


def altTab(tempo):
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')

def pausa():
    altTab(.2)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Sair\n'))
    altTab(.2)
    if optiX == 2:
        exit()

def ctrlC():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def ctrlV():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

def posicaoMouse(time):
    sleep(time)
    print(pyautogui.position())
    
posicaoMouse(5)
posicaoMouse(5)