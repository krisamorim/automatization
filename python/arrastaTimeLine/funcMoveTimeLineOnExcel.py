import pyautogui as pyau
from time import sleep
from subprocess import Popen
import clipboard as clip

pyau.FAILSAFE= False

def altTab(time):
    sleep(time)
    pyau.hotkey('alt','tab')
    sleep(time)

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
    pyau.hotkey('ctrl','home')
    sleep(.6)

def posicaoMouse(waitTime):
    sleep(waitTime)
    print(pyau.position())

def goToCcopyChart(cell,lastPointChart):
    setZoom('50')
    sleep(.5)
    pyau.click(42,171)
    sleep(.4)
    pyau.write(cell)
    sleep(.4)
    pyau.press('enter')
    sleep(.4)
    pyau.keyDown('shiftleft')
    sleep(.4)
    pyau.click(lastPointChart[0],lastPointChart[1])
    sleep(.4)
    pyau.keyUp('shiftleft')
    pyau.hotkey('ctrl','c')
    sleep(.6)
    
def cls():
    Popen(["cls"], shell=True)
    sleep(.5)

def pause(txt):
    altTab(1)
    optiX = int(input(txt))
    if optiX == 2:
        exit()
    altTab(1)

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

def increasingProgressBar(XprogBar, YprogBar, increasing):
    sleep(.6)
    pyau.doubleClick(XprogBar,YprogBar)#click on progressBar
    sleep(.7)
    pyau.click(x=1268, y=112)
    sleep(.3)
    pyau.hotkey('ctrl','c')
    a = clip.paste().replace(' cm','').replace(',','.')
    b = str(float(a)+increasing).replace('.',',')
    pyau.write(b)
    sleep(.4)
    pyau.press('enter')
    # for i in range(1,widthAmount):#increasing progress bar
    #     pyau.click(x=1281, y=108)
    sleep(.6)

def moveBarAndCopyChart(projNumber):
    sleep(.4)
    pyau.click()
    sleep(.4)
    match projNumber:
        case 1:#Senior project
            positions = [420, 452, 484, 516, 540, 575, 600]
            beginningChart = 'C6'
            moveBar = 12
            increaseBar =  1.2
            lastPointChart = [1292, 538]
        case 2:
            print('')

    for i in range(1,moveBar):#move bar
        pyau.press('right')
    sleep(.7)
    for y in positions:
        increasingProgressBar(804, y, increaseBar)
    goToCcopyChart(beginningChart,lastPointChart)
    pause('Check the changes and press 1 to continue or 2 to exit\n>> ')




