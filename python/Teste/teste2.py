import pyautogui
from time import sleep
pyautogui.FAILSAFE= False


def altTab(tempo):
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')

def pausa():
    altTab(.2)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Sair\n'))
    altTab(.2)
    if optiX == 2:
        exit()

def ctrlC():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def ctrlV():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

def comecando():
    #posição da aba do excel
    pyautogui.click(103,21)
    sleep(1)
    pyautogui.click(47,321)
    sleep(1)
    pyautogui.write('J1 ')
    sleep(.5)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('down')
    sleep(.5)
    ctrlC()
    #aba do whatsapp
    pyautogui.click(326, 13)
    sleep(1)
    #clicar no meu chat
    pyautogui.click(151, 311)
    sleep(1)
    pyautogui.write('0')
    sleep(1)
    ctrlV()
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    #clica na mensagem
    pyautogui.click(1200, 628)
    sleep(2)
    #clica no numero
    pyautogui.click(1075, 554)
    sleep(2)
    #posição da aba do excel
    pyautogui.click(103,21)
    sleep(.5)
    pyautogui.press('right')
    sleep(.5)
    ctrlC()
    #aba do whatsapp
    pyautogui.click(326, 13)
    sleep(.5)
    ctrlV()
    sleep(.5)
    pyautogui.press('enter')
    sleep(.5)
    pyautogui.write('Foi enviado um informativo da TI para a execução de um passo a passo no tablet referente ao whatsapp e o outlook (leitor de e-mail. Poderia verificar com o gerente ou a chefia quando será possível executar esse passo a passo ou se já foram realizados  e me dar um retorno?')
    sleep(.5)
    pyautogui.press('enter')
    sleep(1)
    #posição da aba do excel
    pyautogui.click(103,21)
    sleep(1)
    pyautogui.press('down')
    sleep(.5)
    pyautogui.press('left')

def posicaoMouse():
    aaa = pyautogui.position()
    print(aaa)

def continuando():
    ctrlC()
    #aba do whatsapp
    pyautogui.click(326, 13)
    sleep(1)
    #clicar no meu chat
    pyautogui.click(151, 311)
    sleep(1)
    pyautogui.write('0')
    sleep(1)
    ctrlV()
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    #clica na mensagem
    pyautogui.click(1200, 628)
    sleep(2)
    #clica no numero
    pyautogui.click(1075, 554)
    sleep(2)
    #posição da aba do excel
    pyautogui.click(103,21)
    sleep(.5)
    pyautogui.press('right')
    sleep(.5)
    ctrlC()
    #aba do whatsapp
    pyautogui.click(326, 13)
    sleep(.5)
    ctrlV()
    sleep(.5)
    pyautogui.press('enter')
    sleep(.5)
    pyautogui.write('Foi enviado um informativo da TI para a execução de um passo a passo no tablet referente ao whatsapp e o outlook (leitor de e-mail. Poderia verificar com o gerente ou a chefia quando será possível executar esse passo a passo ou se já foram realizados  e me dar um retorno?')
    sleep(.5)
    pyautogui.press('enter')
    sleep(1)
    #posição da aba do excel
    pyautogui.click(103,21)
    sleep(1)
    pyautogui.press('down')
    sleep(.5)
    pyautogui.press('left')

comecando()
pausa()
continuando()
sleep(1)
continuando()
sleep(1)
continuando()