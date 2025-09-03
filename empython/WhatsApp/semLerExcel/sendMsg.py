from time import sleep
import pyautogui
from subprocess import Popen
import os

#--------------------------------definir variaveis-------------------------
pyautogui.FAILSAFE= False
pathOs = os.getcwd()+"/"
# os.chdir (r'z:/Códigos/WhatsApp/semLerExcel/')#linha necessária p/ o locateCenterOnscrren funcionar para localizar imagens
os.chdir (pathOs)#linha necessária p/ o locateCenterOnscrren funcionar para localizar imagens
testMsg = "test"
phones = ['091980590555','091980590555', '091980590555']
#phones = ['04792637808','047999221912', '4784244081']
idSession = ''
setConversa = pyautogui.locateCenterOnScreen('conversar.png')
#-------------------------------Functions---------------------------------
def altTab(tempo):
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')
    sleep(0.5)

def pausa(msgm):
    altTab(1)
    optiX = int(input(msgm))
    altTab(1)
    if optiX == 2:
        exit()

def checkRDS():
    altTab(1)
    Popen(["cls"], shell=True)
    sleep(1)
    optiX = int(input('Pretende fechar o RDS?\n1-Sim\n2-Não\n'))
    if optiX == 1:
        setConversa = (1, 2)
        Popen(["cls"], shell=True)
        sleep(1)
        Popen(["query","session"], shell=True)
        sleep(1)
        print('-'*60)
        idSession = input('Qual o id da sesão exibida acima?\n')
        Popen(["cls"], shell=True)
        sleep(1)
        print('Desconectando em 5 segundos')
        sleep(5)
        id = "rdp-tcp#"+idSession
        Popen(["tscon",id,"/dest:console"], shell=True)
        sleep(5)
        
# altTab(1)
# sleep(1)
# pausa('Whatsapp web ja esta aberto\n1- Sim\n2- Sair\n')
# checkRDS()
sleep(5)
x = pyautogui.position()
print(x)

# for linha in phones:
#     numero = linha
#     pyautogui.click(169, 312) #clicar no proprio zap
#     sleep(2)
#     pyautogui.write(numero) #digitar numero no zap
#     sleep(1)
#     pyautogui.press('enter')
#     sleep(2)
#     pyautogui.click(1162, 629) #clicar no zap
#     sleep(2)
#     try:
#         conversar = setConversa
#         sleep(1)
#         pyautogui.click(conversar)
#         sleep(2)
#         pyautogui.write(testMsg) #Enviar texto
#         sleep(1)
#         pyautogui.press('enter')
#         sleep(2)
#     except pyautogui.ImageNotFoundException:
#         print(numero,' não cadastrado ainda')

altTab(.6)