import pyautogui as pyau
from time import sleep

def selectMenu(menu,submenu,loop):
    menuX = 1
    menuY = 1
    submenuX = 1
    submenuY = 1
    match menu:
        case 'arquivo':
            menuX,menuY = 1        
        case 'formatar':
            menuX = 675
            menuY = 48
        case _:
            print("Valor {} inválido".format(menu))
    pyau.click(menuX,menuY)
    sleep(.5)

    match submenu:
        case 'largura':
            submenuX = 1240
            submenuY = 115   
        case 'aumentarLargura':
            submenuX = 1281
            submenuY = 109
            for i in range(1,loop):
               pyau.click(submenuX,submenuY)
        case _:
            print("Valor {} inválido".format(submenu))
    pyau.click(submenuX,submenuY)

def altTab():
    sleep(.5)
    pyau.hotkey('alt','tab')
    sleep(.5)

def mousePosition(time):
  sleep(time)
  x = pyau.position()
  print(x)

def setZoom(value):
  sleep(.3)
  pyau.click(1341,707)
  sleep(.3)
  pyau.press('tab')
  sleep(.3)
  pyau.write(value)
  sleep(.3)
  pyau.press('enter')
  sleep(.3)

def pause(txt):
  sleep(.5)
  pyau.hotkey('alt','tab')
  optiX = int(input(txt))
  if optiX == 2:
    exit()
  pyau.hotkey('alt','tab')
  sleep(.5)
