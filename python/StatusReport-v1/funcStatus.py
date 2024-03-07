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

def selectAndType(id, idValue, txt, enter):
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

def searchAndClickIMG(path):
    sleep(1)
    attempts = 1
    worked = False
    while worked == False:
        sleep(2)
        try:
            print(f'Trying do locate {path}. Attempts nº {attempts} of 3')
            pyau.click(pyau.locateCenterOnScreen(path))
            worked = True
            status = 'ok'
        except:
            print("locate do id: ",path, " it dosen't work")
            attempts +=1
            status  = 'Nok'
        if attempts == 3:
            worked = True
    return status


    sleep(90)