import pyautogui
from time import sleep
import pyperclip

# sleep(3)
# coordenads = pyautogui.position()
# distanc = 63
# for i in range(3):
#     coordenads = (coordenads[0], coordenads[1]-distanc)
#     pyautogui.moveTo(coordenads)
# sleep(900)

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
projeto = 'Gerente de Projeto Linx - Projeto DPaschoal (02-13/06/2025)'
descr = "elaborar cronograma, daily, status report, comite"

#Questionamento sobre a tela
input(f'Mudou o nome do projeto? ele está como |{projeto}|\n')
input('Entre nos dialogs para carregar as telas primeiro\nDepois retorne aqui e press enter\n')
tela = input('* Enter p/ informar posições\n* 1 p/ utilizar posições p/ tela de 50" c/ tela cheia\n* 2 p/ posições do monitor do notebook\n* 3 p/ posições do monitor do notebook COM TV/MONITOR CONCETADO\n')
pyautogui.hotkey('alt','tab')
sleep(1)

match tela:
    case "":
        #capturar posição do botão "Voltar"
        input('Posicione o mouse sobre o botão "Voltar" e pressione enter\n')
        botaoVoltar = pyautogui.position()
        print(botaoVoltar)
        sleep(1)

        #capturar posição do botão "+ Criar Entrada De hora"
        input('Posicione o mouse sobre o botão "+ Criar Entrada De hora" e pressione enter')
        maisCriarEntradaDeHora = pyautogui.position()
        print('botão "+ Criar Entrada De hora" na posição: ',maisCriarEntradaDeHora)
        pyautogui.click(maisCriarEntradaDeHora)
        sleep(1)
        pyautogui.hotkey('alt','tab')

        #capturar posição do botão "Salvar"
        input('Posicione o mouse sobre o botão "Salvar" e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        botaoSalvar = pyautogui.position()
        print('botão "Salvar" na posição: ',botaoSalvar)
        sleep(1)
        pyautogui.hotkey('alt','tab')

        #capturar posição do botão "X"
        input('Posicione o mouse sobre o botão "X" e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        botaoX = pyautogui.position()
        print(botaoX)
        sleep(1)

    case "1":
        botaoVoltar = (319, 277)
        # maisCriarEntradaDeHora = (2655, 1839)
        maisCriarEntradaDeHora = (1454, 358)
        botaoSalvar = (579, 484)
        botaoX = (3427, 415)

    case "2":
        botaoVoltar = (223, 194)
        maisCriarEntradaDeHora = (1454, 358)
        botaoSalvar = (282, 293)
        botaoX = (1703, 238)

    case "3":
        botaoVoltar = (219, 1265)
        maisCriarEntradaDeHora = (1442, 1637)
        botaoSalvar = (319, 1364)
        botaoX = (1710, 1320)

#clicar na linha selecionada
pyautogui.doubleClick()
sleep(5)

#clicar no botão criar entrada de hora
if tela == "2":
    sleep(3)
    for i in range(5):
        pyautogui.hotkey('ctrl','end')
        sleep(1)

sleep(2)
pyautogui.click(maisCriarEntradaDeHora)
sleep(6)

#Ir para o campo horatrab
for i in range(5):
    pyautogui.press('tab')
    sleep(0.5)
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

#salvar
sleep(1)
pyautogui.click(botaoSalvar)
sleep(20)
pyautogui.click(botaoSalvar)
sleep(20)
pyautogui.click(botaoX)
sleep(5)
pyautogui.click(botaoVoltar)
sleep(2)

#votar para terminal
print('finalizado ', valorDahora)
pyautogui.hotkey('alt','tab')


    
