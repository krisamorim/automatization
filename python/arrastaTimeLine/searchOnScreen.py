import pyautogui
from time import sleep
from subprocess import Popen
pyautogui.FAILSAFE= False

def cls():
    Popen(["cls"], shell=True)
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

def runSearch(imgList):
    cls()
    if locateOnScreenFunc(imgList[0], 2, 1) == False:
        cls()
        if locateOnScreenFunc(imgList[1], 3, 2) == False:
            cls()
            if locateOnScreenFunc(imgList[2], 3, 3) == False:
                exit()