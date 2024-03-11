from selenium import webdriver
from variables import brownserPath
from funcStatus import sleep
from pyautogui import press

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
brownser = webdriver.Chrome(service=service, options=options)
options.binary_location = brownserPath
options.add_argument('--enable-chrome-browser-cloud-management')
# brownser.get(linkSeniorXLSXOnSharePoint)


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
            press('enter')
    return status