from time import sleep
import openpyxl
import pyautogui

#--------------------------------definir variaveis-------------------------
#tempo de espera entre digitações
tempoEsperaIncicio = 2
tempEsperaDigita = 1
tempEsperaClica = 0.5
tempoEsperaEnter = .5
tempCapturaMouse = 5
workbook = openpyxl.load_workbook('zap.xlsx')
pagina = workbook['Planilha1'].iter_rows(min_row=1)
workArray = []
pyautogui.FAILSAFE= False

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
    pyautogui.hotkey('alt','tab')
    sleep(tempo)

def past():
    pyautogui.hotkey('ctrl','v')
    sleep(1)

def pastWhatsUrl():
    pyautogui.hotkey('ctrl', 't')
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
    pyautogui.hotkey('shift','enter')
    sleep(1)
    
def pausa():
    altTab(1)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Sair\n'))
    altTab(1)
    if optiX == 2:
        exit()

sleep(3)
#add no array
for linha in pagina:
    numero = linha[0].value
    pyautogui.click(169, 312) #clicar no proprio zap
    sleep(2)
    pyautogui.write(numero) #digitar numero no zap
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(1162, 629) #clicar no zap
    sleep(2)
    pyautogui.useImageNotFoundException()
    try:
        conversar = pyautogui.locateCenterOnScreen('conversarCom.png')
        sleep(1)
        pyautogui.click(conversar)
        sleep(2)
        pyautogui.write('oi, bom dia. Esse whatsapp é de qual loja? ') #Enviar texto
        sleep(1)
        pyautogui.press('enter')
        sleep(3)
    except pyautogui.ImageNotFoundException:
        print(numero,' não cadastrado ainda')

altTab(1)
