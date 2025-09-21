import pyautogui
from time import sleep
import pyperclip
import sequencialFuncoes as seqFun

#VARIAVEIS-----------------------------------------------------------
projeto = 'Gerente de Projeto Linx - Projeto DPaschoal (16-30/09/2025)'
descr = "elaborar cronograma, daily, status report, comite"
bt_EnviarCom2Monitores = 'img/bt_EnviarCom2Monitores.png'
btMozila_salverCom2Monitores = 'img/btMozila_salverCom2Monitores.png'
btMozila_salverCom2Monitores2 = 'img/btMozila_salverCom2Monitores2.png'
btMozila_salverCom2Monitores3 = 'img/btMozila_salverCom2Monitores3.png'
btMozila_fecharDialog = 'img/btMozila_fecharDialog.png'
btMozila_voltarReservas = 'img/btMozila_voltarReservas.png'

print('Iniciando em 3 seg...')
sleep(3)

#Questionamento sobre nome do projeto
input(f'Mudou o nome do projeto? ele está como |{projeto}|\n')
#Questionamento sobre carregamento das telas
input('Entre nos dialogs para carregar as telas primeiro\nDepois retorne aqui e press enter\n')
#Questionamento sobre a tela
tela = input(f'Qual tela está usando? (1 p/ Monitor do notebook com tela externa conectada e 2 tela do notebook SEM tela externa conectada\n')
match tela:
    case '1':
        print('Usando monitor do notebook com outro monitor conectado\n')
        sleep(2)
        btCriarEntradaX = 1448
        btCriarEntradaY = 1448
        btSalvarEnviarX = 311
        btSalvarEnviarY = 1374
        btFecharDialogX = 1705
        btFecharDialogY = 1322
        btVoltarX = 224
        btVoltarY = 1277
        hrInicialX = 607
        hrInicialY = 1562
    case '2':
        print('Usando monitor do notebook SEM outro monitor conectado\n')
    case _:
        print('Opção inválida, considerando monitor do notebook com outro monitor conectado)\n')
        btCriarEntradaX = 1448
        btCriarEntradaY = 1448
        btSalvarEnviarX = 311
        btSalvarEnviarY = 1374
        btFecharDialogX = 1705
        btFecharDialogY = 1322
        btVoltarX = 224
        btVoltarY = 1277
        hrInicialX = 607
        hrInicialY = 1562

print('Indo para o navegador...')
sleep(3)
pyautogui.hotkey('alt','tab')
sleep(1)

#entrando no dia
seqFun.clickDataAddEntrada()

print('Clicando no botão criar entrada de hora...')
pyautogui.click(btCriarEntradaX, btCriarEntradaY)
sleep(4)

print('Clicando na hora inicial...')
pyautogui.moveTo(hrInicialX, hrInicialY)

#clicar no campo da hora inicial
pyautogui.click()
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.press('tab')
sleep(1)

print('Verificando hora final...')
pyautogui.hotkey('ctrl','c') #copindo valor do campo
sleep(1)
#verificar valor da hora
valorDahora = pyperclip.paste()
if valorDahora == "12:30":
    pyautogui.write("12:00")

print('preenchendo o resto..')
seqFun.tabAndWrite("trab", 2)
seqFun.tabAndWrite(projeto, 4)
seqFun.tabAndWrite("100", 2,"NoENter   ")
seqFun.tabAndWrite("sim", 1)
seqFun.tabAndWrite("prese", 1)
pyautogui.press('tab')
sleep(0.7)
pyautogui.press('tab')

print('colando descrições..')
pyperclip.copy(descr)
sleep(0.7)
for i in range(3):
    seqFun.tabAndWrite(pyperclip.paste(), 1, "NoEnter")
sleep(2)

print('Buscando salvar na tela..')
# seqFun.localizarNaTela(btMozila_salverCom2Monitores3,btMozila_salverCom2Monitores, btMozila_salverCom2Monitores2) #Salvar
pyautogui.moveTo(btSalvarEnviarX, btSalvarEnviarY) #Salvar
sleep(2)
pyautogui.click(btSalvarEnviarX, btSalvarEnviarY) #Salvar
pyautogui.hotkey('alt','tab') 
input('Verifique se salvou corretamente e depois pressione enter para continuar\n')
sleep(1)
pyautogui.hotkey('alt','tab') 

print('Buscando ENVIAR na tela..')
# seqFun.localizarNaTela(bt_EnviarCom2Monitores, bt_EnviarCom2Monitores)
pyautogui.moveTo(btSalvarEnviarX, btSalvarEnviarY) #Enviar
sleep(2)
pyautogui.click(btSalvarEnviarX, btSalvarEnviarY) #Enviar
pyautogui.hotkey('alt','tab') 
input('Verifique se enviou corretamente e depois pressione enter para continuar\n')
pyautogui.hotkey('alt','tab') 
sleep(1)

print('Buscando Fechar na tela..')
# seqFun.localizarNaTela(btMozila_fecharDialog,btMozila_fecharDialog)
pyautogui.click(btFecharDialogX, btFecharDialogY) #Fechar dialog
sleep(4)

print('Buscando "Voltar" na tela..')
# seqFun.localizarNaTela(btMozila_voltarReservas, btMozila_voltarReservas)
pyautogui.click(btVoltarX, btVoltarY) #Voltar
sleep(2)

pyautogui.hotkey('alt','tab')


    
