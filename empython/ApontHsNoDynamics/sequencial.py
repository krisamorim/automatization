import pyautogui
from time import sleep
import pyperclip


#FUNÕES-----------------------------------------------------------
def tabAndWrite(txt, tabs, NoEnter=""):
    sleep(0.7)
    for i in range(tabs):
        pyautogui.press('tab')
    sleep(0.7)
    pyautogui.write(txt)
   
   #verifica se a função recebeu valor em NoEnter
    if NoEnter in (None, ''):
        sleep(2)
        pyautogui.press('enter')
        sleep(1.5)

#VARIAVEIS-----------------------------------------------------------
projeto = 'Gerente de Projeto Linx - Projeto DPaschoal (16-30/06/2025)'
descr = "elaborar cronograma, daily, status report, comite"

#Questionamento sobre a tela
input(f'Mudou o nome do projeto? ele está como |{projeto}|\n')
input('Entre nos dialogs para carregar as telas primeiro\nDepois retorne aqui e press enter\n')

pyautogui.hotkey('alt','tab')
sleep(1)


#clicar no botão criar entrada de hora
pyautogui.click()
pyautogui.press('tab')
sleep(1)
pyautogui.press('tab')
sleep(1)

#Selecionar campo
pyautogui.hotkey('ctrl','c')
sleep(1)
#verificar valor da hora
valorDahora = pyperclip.paste()
if valorDahora == "12:30":
    pyautogui.write("12:00")
# else:
#     for i in range(2):
#         pyautogui.press('tab')
#         sleep(0.5)

# retirar30 = input("Digite 1 p/ remover 30min ou press enter p/ continuar\n")
# retirar30 = "2" if retirar30 != "1" else retirar30
# pyautogui.hotkey('alt', 'tab')
# sleep(1)

# if retirar30 == "1":
#     sleep(0.7)
#     pyautogui.press('backspace')
#     pyautogui.press('backspace')
#     pyautogui.write('00')

tabAndWrite("trab", 2)
tabAndWrite(projeto, 4)
tabAndWrite("100", 2,"NoENter   ")
tabAndWrite("sim", 1)
tabAndWrite("prese", 1)
pyautogui.press('tab')
sleep(0.7)
pyautogui.press('tab')

#Colar descrições das atividades
pyperclip.copy(descr)
sleep(0.7)
for i in range(3):
    tabAndWrite(pyperclip.paste(), 1, "NoEnter")
sleep(2)

#salvar
print('salve')
pyautogui.hotkey('alt','tab')


    
