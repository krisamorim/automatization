from time import sleep
import pyautogui as pyau
import clipboard as clp
from selenium import webdriver
import imgs

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
brownser = webdriver.Chrome(service=service, options=options)
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('--enable-chrome-browser-cloud-management')

brownser.get('https://miliumcombr.sharepoint.com/sites/Onda02-FolhadePagamento/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120008E83637B03E57B41B59039D7E1EFD29C&id=%2Fsites%2FOnda02%2DFolhadePagamento%2FShared%20Documents%2FGeneral%2F1%2E%20Status%20Report&viewid=a88c3865%2D0f79%2D4032%2D9c5d%2D67483c322cde.com')

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
    return status

