import pyautogui as pyau
from time import sleep
from subprocess import Popen
import clipboard as clp

def altTab(tempo):
    sleep(tempo)
    pyau.hotkey('alt','tab')
    sleep(tempo)

def searchOnpage(text):
    sleep(1)
    pyau.hotkey('ctrl','f')
    sleep(1)
    pyau.write(text)
    sleep(1)

def typeWithEnter(text,time):
    sleep(time)
    pyau.write(text)
    sleep(time)
    pyau.press('enter')
    sleep(time)

def ctrlC():
    sleep(.5)
    pyau.hotkey('ctrl', 'c')
    sleep(.5)
    
def ctrlV():
    pyau.hotkey('ctrl', 'v')

def positionMouse(time):
    sleep(time)
    print(pyau.position())

def pausa(msg):
    altTab(1)
    optiX = int(input(msg))
    if optiX == 2:{
        exit()
    }
    altTab(.6)

def clearScreen():
    Popen(["cls"], shell=True)

def searchStore(loja):
    pyau.click(169,12)#click on pasbolt tab
    sleep(1)
    pyau.click(254,182)#click on search bar
    sleep(1)
    pyau.press(['left','left', 'left','left'])#go to begin of the search bar input
    sleep(.5)
    pyau.press(['del','del', 'del', 'del'])
    sleep(.5)
    pyau.write('a'+loja)
    sleep(1)
    pyau.press('enter')
    sleep(1.2)
    pyau.click(710, 351)#copy pass
    sleep(2)
    print('Loja {}: {}'.format(loja, clp.paste()))
    sleep(.6)

def checkPageLoad(whatCheck,whatCheck2,x,y):
    oldCLipBoard = clp.paste()
    load = ''
    while load != whatCheck and load != whatCheck2:
        sleep(3)
        pyau.doubleClick(x,y)
        sleep(1)
        pyau.hotkey('ctrl','c')
        sleep(1)
        load = clp.paste().lstrip().rstrip()
    clp.copy(oldCLipBoard)

def accesUrl():
    pyau.click(901, 360)#click on url link in pasbol page
    checkPageLoad('não','não',528,322)#wait login page load
    sleep(1)
    pyau.click(402, 500)
    sleep(1)
    pyau.click(476, 658)
    sleep(4)
    pyau.click(665,154)
    sleep(4)
    pyau.write('admin')
    sleep(1)
    pyau.press('tab')
    sleep(1)
    pyau.write(clp.paste())
    sleep(1)
    pyau.press('enter')
    sleep(1)

def accessFWproxypage(store):
    # store = store.replace("0","")#
    store = store.replace("0","") if store[0] == '0' else store
    urlpol = 'https://192.168.'+store+'.254:10443/cgi-bin/proxypolicy.cgi'
    sleep(1)
    checkPageLoad('Painel','Dashboard',399 ,259)
    sleep(1)
    print("Acessando "+urlpol)
    sleep(1)
    pyau.hotkey('ctrl','l')
    sleep(1)
    pyau.press('del')
    sleep(1)
    pyau.write(urlpol)
    sleep(2)
    pyau.press('enter')
    sleep(6)
    # pyau.click(822, 207)#click on proxy link
    # sleep(2)
    # pyau.click(503, 294)#click on access policies
    checkPageLoad('Destino','target',545,373)
    sleep(1)
    searchOnpage('filtrado')
    sleep(.7)
    pyau.click(1083, 367)#click on edit
    checkPageLoad('MIME','MIME',772,624)#check if page load
    pyau.click(852,426)
    sleep(.5)
    pyau.hotkey('ctrl','a')
    # pausa('funcionou?\n1-SIM\n2-NÃO\n')
    sleep(.5)
    ctrlC()
    
def typeTextPerRow(array):
    total = len(array)
    for i in array:
        typeWithEnter(i,1)
        total -=1
        print('{} digitado. Falta {}'.format(i,total))

def saveData(store,list):
    fileBefore = '%userprofile%/desktop/loja'+store+'-1regraBCKP.txt'
    fileAfter = '%userprofile%/desktop/loja'+store+'-1regraUPDTED.txt'
    sleep(1)
    #before
    Popen(["type", 'nul',">", fileBefore], shell=True)
    print('salvando no arquivo '+fileBefore)
    sleep(1)
    Popen(["start", fileBefore], shell=True)
    sleep(2)
    ctrlV()
    sleep(2)
    pyau.hotkey('ctrl','s')
    sleep(1)
    pyau.hotkey('alt','f4')
    sleep(2)

    #after
    Popen(["type", 'nul',">", fileAfter], shell=True)
    sleep(1)
    Popen(["start", fileAfter], shell=True)
    sleep(2)
    ctrlV()
    sleep(1.5)
    for rule in list:
        pyau.press('enter')
        sleep(1)
        pyau.write(rule)
    pyau.hotkey('ctrl','a')
    sleep(.5)
    ctrlC()
    pyau.hotkey('ctrl', 's')
    print('salvando no arquivo '+fileAfter)
    sleep(1)
    pyau.hotkey('alt','f4')
    sleep(1)
    pyau.click(852,426)
    sleep(.5)
    pyau.hotkey('ctrl','a')
    ctrlV()
    searchOnpage('or c')
    pyau.click(453,413)#click on pudate policy
    sleep(2)

    #searching 2nd rule
    searchOnpage('filtrado')
    pyau.press('enter')
    sleep(.7)
    pyau.click(1083, 367)#click on edit
    sleep(4)
    pyau.click(746,531)#clique on rule field
    sleep(.5)
    pyau.hotkey('ctrl','a')
    # pausa('funcionou?\n1-SIM\n2-NÃO\n')
    sleep(.5)
    ctrlC()

    file2Before = '%userprofile%/desktop/loja'+store+'-2regraBCKP.txt'
    file2After = '%userprofile%/desktop/loja'+store+'-2regraUPDTED.txt'
    sleep(1)
    #before
    Popen(["type", 'nul',">", file2Before], shell=True)
    print('salvando no arquivo '+file2Before)
    sleep(1)
    Popen(["start", file2Before], shell=True)
    sleep(2)
    ctrlV()
    sleep(2)
    pyau.hotkey('ctrl','s')
    sleep(1)
    pyau.hotkey('alt','f4')
    sleep(2)

    #after
    Popen(["type", 'nul',">", file2After], shell=True)
    sleep(1)
    Popen(["start", file2After], shell=True)
    sleep(2)
    ctrlV()
    sleep(1.5)
    for rule in list:
        pyau.press('enter')
        sleep(1)
        pyau.write(rule)
    pyau.hotkey('ctrl','a')
    sleep(.5)
    ctrlC()
    pyau.hotkey('ctrl', 's')
    print('salvando no arquivo '+file2After)
    sleep(1)
    pyau.hotkey('alt','f4')
    sleep(1)
    pyau.click(746,531)#click on rule field
    sleep(.5)
    pyau.hotkey('ctrl','a')
    ctrlV()
    searchOnpage('or c')
    pyau.click(453,413)#click on pudate policy
    sleep(4)
    # searchOnpage('aplicar')
    # sleep(1)
    pyau.click(625,386)