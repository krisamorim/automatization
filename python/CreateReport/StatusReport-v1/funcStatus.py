from time import sleep
import pyautogui as pyau
import clipboard as clip
from subprocess import Popen
import credntials as cred
import variables as vari

def __init__():
    print('')

def setProj(ProjectNumbver):
    match ProjectNumbver:
        case 1:
            urlProject = cred.linkSeniorXLSXOnSharePoint
            listProgressBar = vari.SRpositions
            beginningChart = vari.SRbeginningChart
            moveBar = vari.SRmoveBar
            increaseBar =  vari.SRincreaseBar
            lastPointChart = vari.SRlastPointChart
            slideTitle = vari.SRslideTitle
            downImgOnPPT = vari.SRdownImgOnPPT
        case 2:
            urlProject = cred.linkCVXLSXOnSharePoint
            listProgressBar = vari.CVpositions
            beginningChart = vari.CVbeginningChart
            moveBar = vari.CVmoveBar
            increaseBar =  vari.CVincreaseBar
            lastPointChart = vari.CVlastPointChart
            slideTitle = vari.CVslideTitle
            downImgOnPPT = vari.CVdownImgOnPPT
        case 3:
            urlProject = cred.linkOrcamXLSXOnSharePoint
            listProgressBar = vari.budGetpositions
            beginningChart = vari.budGetbeginningChart
            moveBar = vari.budGetmoveBar
            increaseBar =  vari.budGetincreaseBar
            lastPointChart = vari.budGetlastPointChart
            slideTitle = vari.budGetslideTitle
            downImgOnPPT = vari.budGetdownImgOnPPT

    return {'urlProject': urlProject, 'listProgressBar': listProgressBar, 'beginningChart': beginningChart, 'moveBar': moveBar, 'increaseBar': increaseBar, 'lastPointChart': lastPointChart, 'slideTitle': slideTitle, 'downImgOnPPT': downImgOnPPT} 

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

def doublePause(txt):
    pyau.keyDown('alt')
    pyau.press(['tab','tab'])
    sleep(.8)
    pyau.keyUp('alt')
    sleep(1)
    optiX = int(input(txt))
    if optiX == 2:
        exit()
    altTab(.7)

def maxWindow():
    pyau.hotkey('alt','space')
    sleep(1)
    pyau.press('x')

def locateOnScreenFunc(files, tentativas, timeToWaiting):#informe array with img's path, amount of attempts and time to wait bettwen attempts
    status = False
    for file in files:
        if status == True:
            print('Imagem encontrada')
        else:
            contador=0
            attempts=contador+1
            while contador < tentativas:#enquanto o contador for menor que o numero de tentativas informado na função
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
                    timeToWaiting = .2
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
    pyau.press('alt')
    sleep(.6)
    pyau.press('k')
    sleep(.6)
    pyau.press('b')
    sleep(.3)
    pyau.press('o')
    # pyau.click(1341,707)
    sleep(.5)
    pyau.press('tab')
    sleep(.5)
    pyau.write(value)
    sleep(.5)
    pyau.press('enter')
    sleep(.6)
    pyau.hotkey('ctrl','home')
    sleep(.6)
    pyau.press('alt')
    sleep(.6)
    pyau.press('c')
    sleep(.3)

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
    pyau.doubleClick()
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
    doublePause('Check the changes and press 1 to continue or 2 to exit\n>> ')
#---Function above to edit em copy chart in excel file

def gotToSlide(projNumber):
    sleep(.7)
    pyau.hotkey('ctrl','l')
    sleep(.6)
    pyau.hotkey('ctrl','a')
    sleep(.6)
    pyau.press('del')
    sleep(.6)
    pyau.write(setProj(projNumber)['slideTitle'])
    sleep(.1)
    pyau.press(['tab','tab','enter'])
    sleep(.1)
    pyau.press(['esc','esc','esc','esc'])
    sleep(.6)

def updateImageOnPPT(projNumber):
    sleep(.5)
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
    for i in range(1,setProj(projNumber)['downImgOnPPT']):
        pyau.press('down')
    pyau.click(813, 72)
    sleep(1.5)
    pyau.click(789, 165)
    sleep(.5)
    #set animation
    pyau.click(417, 44) #animation menu
    sleep(.7)
    pyau.click(615, 95) #erease option
    sleep(.7)
    pyau.click(778, 107) #efect option
    sleep(.7)
    pyau.click(795, 306) #down option efect
    sleep(.7)
    sleep(1.2)
    for i in range(1,9):
        pyau.click(1254, 93) #move animatioin to up
    sleep(.7)
    for i in range(1,3):
        pyau.click(1233, 119) #move animation do down
    sleep(1)

