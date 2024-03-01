import pyautogui
from time import sleep
from subprocess import Popen
import os
pyautogui.FAILSAFE= False
os.chdir('.\searchOnScreen')
files = ['excelTitlebar.png','excelFunctionTitle.png','excelCopy.png']
file = os.path.abspath(files[0])
executar = 1

def pause(txt):
  pyautogui.hotkey('alt','tab')
  optiX = int(input(txt))
  if optiX == 2:
    exit()
  pyautogui.hotkey('alt','tab')
  sleep(.5)

def locateOnScreenFunc(file, tentativas, timeToWaiting):
    contador=0
    status = False
    while contador < tentativas:
        try:
            location = pyautogui.locateOnScreen(file)
            print(f'image {file} found!')
        except pyautogui.ImageNotFoundException:
            print(f'Image {file} not found')
            location = False
        print(f'Valor de location na tentativa nº {contador}: {location}')
        if location != False:
            contador = tentativas
            status = True
            pyautogui.moveTo(location, duration=.5)
        contador+=1
        sleep(timeToWaiting)
    return status

        # search = pyautogui.locateCenterOnScreen(path)
        # if search != None:
        # 
        # if search != None:
        #     print(f'Imagem localizada em {search}')
        #     pyautogui.moveTo(search, duration=.2)
        #     pyautogui.click()

        # if contador>=tentativas:
        #     print(f'Tentativa nº {contador} sem sucesso')
        # sleep(.25)

while executar == 1:
    Popen(["cls"], shell=True)
    sleep(.5)
    if locateOnScreenFunc(files[0], 2, 1) == False:
        if locateOnScreenFunc(files[1], 3, 2) == False:
            if locateOnScreenFunc(files[2], 3, 3) == False:
                pause('Digite 1 p/ continuar ou 2 p/ sair\n>> ')
            else:
                executar = 2