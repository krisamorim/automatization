import pyautogui as pyau
from time import sleep
import variables as var
from subprocess import Popen 
pyau.FAILSAFE= False

def cls():
    Popen(["cls"], shell=True)

def clickNo():
    pyau.click(712, 451)
    sleep(2)

def altTab(tempo):
    sleep(tempo)
    pyau.hotkey('alt','tab')
    sleep(1)

def pausa():
    altTab(.6)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Repetir\n3- Sair\n>> '))
    if optiX == 3:
        exit()
    if optiX == 2:
        altTab(.6)
    return optiX

def primeiroProdu(quant1stprod, cod1stProdu):
    sleep(1)
    pyau.click(781, 154)
    pyau.write(quant1stprod)
    pyau.press('enter')
    sleep(.6)
    pyau.write(cod1stProdu)
    sleep(.6)
    pyau.press('enter')
    sleep(.6)
    clickNo()
    sleep(3)

def duasVendasNoKitNoPrimeiVenda(qntd1prod,cod1prod,qntd2prod,cod2prod):
    #digitando qntidade do 1 produto
    sleep(1)
    pyau.click(781, 154)
    pyau.write(qntd1prod)
    pyau.press('enter')
    sleep(0.2)
    #digitando codigo do 2 produto
    pyau.write(cod1prod)
    sleep(.6)
    pyau.press('enter')
    sleep(.2)
    #digitando qntidade do 2 produto
    sleep(1)
    pyau.click(781, 154)
    pyau.write(qntd2prod)
    pyau.press('enter')
    sleep(0.2)
    #digitando codigo do 2 produto
    pyau.write(cod2prod)
    sleep(.6)
    pyau.press('enter')
    sleep(.2)

def venda(qntid,prod):
    sleep(3)
    pyau.click(781, 154)
    pyau.write(qntid)
    pyau.press('enter')
    sleep(.6)

    #digitando codigo doproduto
    pyau.write(prod)
    sleep(.6)
    pyau.press('enter')
    sleep(2)

def finalizarVenda():
    pyau.press('f12')
    sleep(2)
    pyau.press('enter')
    sleep(1)
    pyau.press('enter')
    sleep(1)
    pyau.press('enter')
    sleep(7)
    clickNo()

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
                    location = pyau.locateOnScreen(file)
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

def loginPdv():#to type password
    status = True
    if locateOnScreenFunc(var.listImgsLoginPage,2,2):
        pyau.click()
        sleep(.5)
        pyau.write(var.passPDV)
        sleep(.7)
        pyau.press('enter')
        sleep(10)
        if locateOnScreenFunc(var.listImgsLoginPage,2,2):
            pyau.click()
            sleep(1)
    else:
        status = False
        sleep(1)
        pyau.press('f2')
        print('login page not found. Searching sales screen')
        if locateOnScreenFunc(var.listImgsSalesScreen,2,2):
            print('Pagina de vendas encontrada')


#apagar
# def searchImg(img):
#     attempt = 1
#     status = ''
#     xy = ''
#     while attempt <= 3:
#         try:
#             print(f'Trying to locate {img}. Attempt {attempt} of 3:')
#             xy = pyau.locateCenterOnScreen(img, confidence=.6)
#             status = 'ok'
#             attempt = 4
#         except:
#             print('not found')
#             attempt +=1
#             status = 'Nok'
#         sleep(2)
#     return [status, xy]
        
# def searchAndClick(pathImg):
#     continuar = 2
#     while continuar == 2:
#         xy = searchImg(pathImg)
#         if xy[0] =='Nok':
#             print('PDVonTaskBar not found')
#             continuar = pausa()
#         else: 
#             pyau.click(xy[1])
#             continuar = 3
#         sleep(1)
