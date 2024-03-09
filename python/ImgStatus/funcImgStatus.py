from time import sleep
import pyautogui as pyau
from subprocess import Popen
#--------------------------------definir variaveis-------------------------
pyau.FAILSAFE= False

#--------------------------------definir funções-------------------------
# def posiMouse(waitTime):
    # sleep(waitTime)
    # x = pyau.position()
    # print(x)
    
def altTab(tempo):
    pyau.hotkey('alt','tab')
    sleep(tempo)

def updateImage(down):
    pyau.click(416, 340)
    sleep(.7)
    pyau.press('del')
    sleep(.5)
    pyau.hotkey('ctrl','alt','v')
    sleep(.5)
    pyau.press(['tab','b','b'])
    sleep(.5)
    pyau.press('enter')
    sleep(.5)
    pyau.doubleClick(416, 340)
    sleep(0.5)
    pyau.click(1264, 110)
    sleep(.7)
    pyau.write('32,8')
    sleep(1)
    pyau.press('enter')
    sleep(.5)
    pyau.click(1105, 79)
    sleep(.7)
    pyau.click(1133, 120)
    sleep(.7)
    for i in range(1,down):
        pyau.press('down')
    pyau.click(813, 72)
    sleep(1.5)
    pyau.click(789, 165)

def animacao():
    sleep(.7)
    pyau.click(417, 44) #animation menu
    sleep(.7)
    pyau.click(615, 95) #erease option
    sleep(.7)
    pyau.click(778, 107) #efect option
    sleep(.7)
    pyau.click(795, 306) #down option efect
    sleep(.7)
    # pyau.click(980, 75) #animation painel
    sleep(1.2)
    for i in range(1,9):
        pyau.click(1254, 93) #move animatioin to up
    sleep(.7)
    for i in range(1,3):
        pyau.click(1233, 119) #move animation do down
    sleep(1)

def pause(txt):
    altTab(1)
    optiX = int(input(txt))
    if optiX == 2:
        exit()
    altTab(1)

def cls():
    Popen('cls', shell=True)
    sleep(1)
    
def option():
    status = int(input('Qual Oção?\n1 p/ Proj Sr\n2 p/ Proj CV\n3 p/ Proj Orcam\n4 p/ Proj Novas Lojas\n5 p/ Proj Adquirência\n6 p/ Proj ADSL\n7 p/ Proj Dr\n8 p/ Proj Zimbra\n9 p/ Proj Telefonia\n0 p/ Sair\n>> '))
    match status:
        case 1: downKey = 16
        case 2: downKey = 16
        case 3: downKey = 17
        case 4: downKey = 21
        case 5: downKey = 14
        case 6: downKey = 14
        case 7: downKey = 14
        case 8: downKey = 14
        case 9: downKey = 14
        case 0: exit()
    return downKey    
