import pyautogui as pyau
from time import sleep

def altTab(tempo):
    pyau.keyDown('alt')
    sleep(tempo)
    pyau.press('tab')
    sleep(tempo)
    pyau.keyUp('alt')
    
def ctrlC():
    pyau.keyDown('ctrl')
    pyau.press('c')
    pyau.keyUp('ctrl')

def ctrlV():
    pyau.keyDown('ctrl')
    pyau.press('v')
    pyau.keyUp('ctrl')

def posicaoMouse():
    aaa = pyau.position()
    print(aaa)

def pausa(msg):
    optiX = int(input(msg))
    if optiX == 2:
        exit()