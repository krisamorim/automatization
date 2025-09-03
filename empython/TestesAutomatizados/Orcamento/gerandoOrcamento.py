import pyautogui
from time import sleep
pyautogui.FAILSAFE= False

#--------------------------------definir variaveis-------------------------
#tempo de espera entre digitações
timeClickWriteEnter = .5
waitingPageLoad = 7
userNamePortal = "85989142234"
cpfCustomer = ('09897092994','04982793913')
prod1 = ('1007199', '1') #porca sext BCa
prod2 = ('1000572','2') #aruela lisa
prod3 = ('1002260','3') #cadeado
prod4 = ('1000884','5') #chave philips
prod5 = ('1004760','1') #Eletrodo

#--------------------------------definir funções-------------------------
def altTab(tempo):
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')
    sleep(tempo)

def pausa():
    altTab(.2)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Sair\n'))
    altTab(.2)
    if optiX == 2:
        exit()
    print('Seguindo...')

def acessarURL(userName):
    #typing URL------------------------------------
    pyautogui.click(483, 57)
    sleep(timeClickWriteEnter)
    pyautogui.write("portalhml.milium.com.br")
    sleep(timeClickWriteEnter)
    pyautogui.press('enter')
    sleep(waitingPageLoad)
    #typing username-------------------------------
    pyautogui.click(622, 438)
    sleep(timeClickWriteEnter)
    pyautogui.write(userName)
    sleep(timeClickWriteEnter)
    pyautogui.press('tab')
    pausa()
    sleep(waitingPageLoad)

def setStore1InLogin():
    sleep(timeClickWriteEnter)
    pyautogui.click(625, 401)
    sleep(timeClickWriteEnter)
    pyautogui.press('tab')
    sleep(timeClickWriteEnter)
    pyautogui.press('backspace')
    pyautogui.write('0')
    sleep(timeClickWriteEnter)
    pyautogui.press('down')
    sleep(timeClickWriteEnter)
    pyautogui.press('enter')
    pyautogui.click(723, 530)

def addProducBudget(prod, qntd):
    sleep(3)
    pyautogui.click(539, 239) #click on product tab
    sleep(3)
    pyautogui.click(584, 324) #click on product field
    sleep(1)
    pyautogui.write(prod) #Add product
    sleep(.5)
    pyautogui.press('enter')
    sleep(4)
    #pyautogui.click(719, 431) #click on product qntid field
    sleep(1)
    pyautogui.press('backspace')
    sleep(1)
    pyautogui.write(qntd)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('enter')

def addPayment():
    sleep(1)
    pyautogui.click(706, 248) #click on payment field
    sleep(4)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.click(320, 195) #click on budget finish button
    sleep(4)

def createBudget():
    sleep(3)
    pyautogui.click(412, 321) #click on budget button
    sleep(4)
    pyautogui.click(263, 287) #click on + button
    sleep(4)

def addCustomer(customerCPF):
    pyautogui.click(512, 322) #click on customer id field
    sleep(3)
    pyautogui.write(customerCPF) #write cpf user
    sleep(1)
    pyautogui.press('enter')
    sleep(5)

def savePDF():
    pyautogui.click(208, 186) #click on pdf save button
    sleep(4)
    pyautogui.click(1228, 125) #click on close
    sleep(2)
    pyautogui.click(1348, 710) #click on close down view
    sleep(2)

def getMousePosition():
    x = pyautogui.position()
    print(x)

altTab(1)
#acessarURL(userNamePortal)
#setStore1InLogin()
#sleep(1)
#createBudget()
#addCustomer(cpfCustomer[0])
addProducBudget(prod2[0], prod2[1])
sleep(2)
addProducBudget(prod1[0], prod1[1])
sleep(2)
addProducBudget(prod3[0], prod3[1])
sleep(2)
addProducBudget(prod5[0], prod5[1])
addPayment()
savePDF()
altTab(1)

#print(prod1['cod'], "  ", prod1['qnt'])
# prod1 = {'cod': '1004199', 'qnt': '1'}
# prod2 = {'cod': '1000572', 'qnt': '2'}
# products = (prod1, prod2)
# print(products[])
#
# 