import pyautogui as pyau
from time import sleep
from subprocess import Popen
pyau.FAILSAFE= False

def altTab():
    sleep(.5)
    pyau.hotkey('alt','tab')
    sleep(.5)

def setZoom(value):
    sleep(.6)
    pyau.click(1341,707)
    sleep(.5)
    pyau.press('tab')
    sleep(.5)
    pyau.write(value)
    sleep(.5)
    pyau.press('enter')
    sleep(.6)

def posicaoMouse(waitTime):
    sleep(waitTime)
    print(pyau.position())

def cls():
    Popen(["cls"], shell=True)
    sleep(.5)

def locateOnScreenFunc(files, tentativas, timeToWaiting):#informe array with img's path, amount of attempts and time to wait bettwen attempts
    status = False
    for file in files:
        if status == True:
            print('Imagem encontrada')
        else:
            contador=0
            attempts=contador+1
            while contador < tentativas:
                print(f'Tentativa Nº {attempts}')
                try:
                    location = pyau.locateOnScreen(file, confidence=.9)
                    print(f'image {file} found!')
                except pyau.ImageNotFoundException:
                    print(f'Image {file} not found')
                    location = False
                    contador+=1
                    attempts+=1
                if location != False:
                    contador = tentativas
                    status = True
                    pyau.moveTo(location, duration=.4)
                    timeToWaiting = .1
                sleep(timeToWaiting)
    return status

def moveBar(projName):
    sleep(.4)
    pyau.click()
    match projName:
        case 1:
            for i in range(1,12):
                pyau.press('right')

