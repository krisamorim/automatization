from time import sleep
import pyautogui as pyau
import clipboard as clip
from subprocess import Popen
import credntials as cred
import variables as vari

def setProj(ProjectNumbver):
    match ProjectNumbver:
        case 1:
            urlProject = cred.linkSeniorXLSXOnSharePoint
            listProgressBar = vari.SRpositions
            beginningChart = vari.SRbeginningChart
            moveBar = vari.SRmoveBar
            increaseBar =  vari.SRincreaseBar
            lastPointChart = vari.SRlastPointChart
        case 2:
            urlProject = cred.linkCVXLSXOnSharePoint
            listProgressBar = vari.CVpositions
            beginningChart = vari.CVbeginningChart
            moveBar = vari.CVmoveBar
            increaseBar =  vari.CVincreaseBar
            lastPointChart = vari.CVlastPointChart
    return {'urlProject': urlProject, 'listProgressBar': listProgressBar, 'beginningChart': beginningChart, 'moveBar': moveBar, 'increaseBar': increaseBar, 'lastPointChart': lastPointChart} 

def cls():
    Popen(["cls"], shell=True)
    sleep(1)

def altTab(time):
    sleep(time)
    pyau.hotkey('alt','tab')
    sleep(time)

def pause(txt):
    altTab(.7)
    optiX = int(input(txt))
    if optiX == 2:
        exit()
    altTab(.7)

def maxWindow():
    pyau.hotkey('alt','space')
    sleep(.8)
    pyau.press('x')

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

def searchAndClickIMG(files, tentativas, timeToWaiting):
    sleep(1)
    locateOnScreenFunc(files, tentativas, timeToWaiting)
    sleep(.5)
    pyau.click()
    sleep(.5)

#---Function below to edit em copy chart in excel file
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
    sleep(.6)

def moveBarAndCopyChart(projNumber):
    sleep(.4)
    pyau.click()
    sleep(.4)
    moveBar = setProj(projNumber)['moveBar']
    positions = setProj(projNumber)['listProgressBar']
    beginningChart = setProj(projNumber)['beginningChart']
    increaseBar = setProj(projNumber)['increaseBar']
    lastPointChart = setProj(projNumber)['lastPointChart']

    for i in range(1,moveBar):#move bar
        pyau.press('right')
    sleep(.7)
    for y in positions:
        increasingProgressBar(804, y, increaseBar)
    goToCcopyChart(beginningChart,lastPointChart)
    pause('Check the changes and press 1 to continue or 2 to exit\n>> ')
#---Function above to edit em copy chart in excel file
