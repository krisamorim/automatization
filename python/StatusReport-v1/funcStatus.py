from time import sleep
import pyautogui as pyau
import clipboard as clp
from selenium import webdriver
import variables as vari

print(vari.ImglinkProjetoSenior)

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
brownser = webdriver.Chrome(service=service, options=options)
options.binary_location = vari.brownserPath
options.add_argument('--enable-chrome-browser-cloud-management')

brownser.get(vari.linkSeniorXLSX)

def maxWindow():
    pyau.hotkey('alt','space')
    sleep(.6)
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

def selectAndClik(id, idValue):
    sleep(1)
    attempts = 1
    worked = False
    while worked == False:
        sleep(2)
        try:
            print(f'Trying do locate {idValue}. Attempts nº {attempts} of 3')
            brownser.find_element(id, idValue).click()
            worked = True
            status = 'ok'
        except:
            print("locate do id: ",idValue, " it dosen't work")
            attempts +=1
            status  = 'Nok'
        if attempts == 3:
            worked = True
    return status

def selectAndClikRight(id, idValue):
    sleep(1)
    attempts = 1
    worked = False
    while worked == False:
        sleep(2)
        try:
            print(f'Trying do locate {idValue}. Attempts nº {attempts} of 3')
            brownser.find_element(id, idValue).click(2)
            worked = True
            status = 'ok'
        except:
            print("locate do id: ",idValue, " it dosen't work")
            attempts +=1
            status  = 'Nok'
        if attempts == 3:
            worked = True
    return status

def selectAndType(id, idValue, txt):
    sleep(1)
    attempts = 1
    worked = False
    while worked == False:
        sleep(3)
        try:
            print(f'Trying do locate {idValue}. Attempts nº {attempts} of 3')
            brownser.find_element(id, idValue).send_keys(txt)
            worked = True
            status = 'ok'
        except:
            print("locate do id: ",idValue, " it dosen't work")
            attempts +=1
            status  = 'Nok'
        if attempts == 4:
            worked = True
        if status == 'ok':
            pyau.press('enter')
    return status

def searchAndClickIMG(files, tentativas, timeToWaiting):
    sleep(1)
    locateOnScreenFunc(files, tentativas, timeToWaiting)
    sleep(.5)
    pyau.click()
    sleep(.5)