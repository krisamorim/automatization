import pyautogui
from time import sleep
pyautogui.FAILSAFE= False

#--------------------------------definir variaveis-------------------------
#tempo de espera entre digitações
tempoEsperaIncicio = 2
tempEsperaDigita = 1
tempEsperaClica = 0.5
tempoEsperaEnter = .5
tempCapturaMouse = 5
columnAndRow = 'J1'
#--------------------------------definir funções-------------------------
def goTo1stCel(coluAndRow):
    pyautogui.click(37, 326)
    sleep(tempEsperaClica)
    pyautogui.write(coluAndRow)
    sleep(tempEsperaDigita)
    pyautogui.press('enter')
    sleep(tempoEsperaEnter)

def posiMouse(waitTime):
    sleep(waitTime)
    x = pyautogui.position()
    print(x)

def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    sleep(1)
    pyautogui.keyUp('ctrl')
    
def altTab(tempo):
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')
    sleep(tempo)

def past():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    sleep(1)
    pyautogui.keyUp('ctrl')

def pastWhatsUrl():
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    sleep(1)
    pyautogui.keyUp('ctrl')
    pyautogui.write('https://web.whatsapp.com/send/?phone=55')
    sleep(.5)
    past()
    pyautogui.write('&text=')
    sleep(.5)
    altTab(1)
    pyautogui.press('right')
    sleep(.5)
    copy()
    sleep(.5)
    altTab(1)
    past()
    sleep(1)
    pyautogui.write('&type=phone_number&app_absent=0')
    pyautogui.press('enter')
    sleep(10)
    pyautogui.press('enter')

def blWhats():
    sleep(1)
    pyautogui.keyDown('shift')
    sleep(1)
    pyautogui.press('enter')
    pyautogui.keyUp('shift')
    
sleep(5)

goTo1stCel(columnAndRow)
pyautogui.press('down')
copy()
altTab(1)
pastWhatsUrl()
sleep(4)
pyautogui.write('Ha alguns dias atrás foi enviado um informativo para configurar o whatsapp no tablet, colocar a logomarca da milium como imagem de perfil e definir uma mensagem automatica.')
blWhats()
pyautogui.write('Sabe me informar se foi feito?')
pyautogui.press('enter')

posiMouse(tempCapturaMouse)

