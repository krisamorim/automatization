from selenium import webdriver
from time import sleep
import pyautogui as pyau
import clipboard as clp

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
brownser = webdriver.Chrome(service=service, options=options)
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('--enable-chrome-browser-cloud-management')

def typeText(ID, IDVALUE, TXT):
    brownser.find_element(ID, IDVALUE).send_keys(TXT) 

def gotToUrl(urlToaccess):
    brownser.get(urlToaccess)

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

def selectAndType(id, idValue, txt):
    sleep(1)
    attempts = 1
    worked = False
    while worked == False:
        sleep(2)
        try:
            print(f'Trying do locate {idValue}. Attempts nº {attempts} of 3')
            brownser.find_element(id, idValue).send_keys(txt)
            worked = True
            status = 'ok'
        except:
            print("locate do id: ",idValue, " it dosen't work")
            attempts +=1
            status  = 'Nok'
        if attempts == 3:
            worked = True
    return status

def loginPage(listData):
    sleep(1)
    brownser.find_element(listData[0], listData[1]).send_keys(listData[2]) 
    brownser.find_element(listData[0], listData[3]).send_keys(listData[4])
    brownser.find_element(listData[0], listData[3]).submit()
    sleep(2)

def setEstabelecimento(listDataMenu):
    sleep(1)
    exit() if selectAndClik(listDataMenu[0], listDataMenu[1]) == 'Nok' else print('Estabelec')
    exit() if selectAndClik(listDataMenu[2], listDataMenu[3]) == 'Nok' else print('Next')

def goToUserStorePage(listMenuUserStore):
    sleep(1)
    selectAndClik(listMenuUserStore[0], listMenuUserStore[1])
    sleep(2)
    selectAndClik(listMenuUserStore[2], listMenuUserStore[3])
    sleep(2)
    
def addUserAlreadyExist():
    print('add user already exist')

def addUserNotAlreadyExist(name):
    selectAndClik('id','f_nome')
    sleep(1)
    saveOldValueCtrlV = clp.paste()
    clp.copy(" ")
    pyau.hotkey('ctrl','a')
    sleep(.5)
    pyau.hotkey('ctrl','c')
    if clp.paste() == " ":
        selectAndType('id', 'f_nome', name)

    # print('add user NOT exist')