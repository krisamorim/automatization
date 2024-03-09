import pyautogui as pyau
import searchOnScreen as sos
from time import sleep
import os
pyau.FAILSAFE= False
pathCode = os.path.join(os.getcwd(), 'Millium\\arrastaTimeLine')
os.chdir(pathCode)
imgList = ['timeLineBar1.png', 'timeLineBar2.png', 'timeLineBar3.png']
x = 28 #10 para um quadrado somente e 41 p/ 5
x *=4
def altTab():
    pyau.PAUSE = 0.6
    pyau.hotkey('alt','tab')
    # pyau.PAUSE()

def posicaoMouse():
    print(pyau.position())

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

altTab()
# setZoom('70')
sos.runSearch(imgList)
pyau.click()
sleep(.6)
for i in range(1,x):
    pyau.press('right')
    # sleep(.1)
# setZoom('50')
sleep(1)
altTab(.6)