import pyautogui
from time import sleep
import pyperclip
import sequencialFuncoes as seqFun
import sequencialVariables as seqVar

print('Iniciando em 3 seg...')
sleep(3)
#Questionamento sobre nome do projeto
input(f'Mudou o nome do projeto? ele está como |{seqVar.projeto}|\n')
#Questionamento sobre carregamento das telas
input('Entre nos dialogs para carregar as telas primeiro. Depois retorne aqui e press enter\n')
#Questionamento sobre a tela
tela = input(f'Qual tela está usando?\n(1 p/ Monitor do notebook com tela externa conectada e 2 tela do notebook SEM tela externa conectada\n')
#Verificando quantas vezes deseja repetir o código
repeticaoVezes = input("Quantas vezes deseja repetir o processo? (Digite um número): \n")
if not repeticaoVezes.isdigit() or int(repeticaoVezes) <= 0:
    repeticaoVezes = 1
    print("Entrada inválida. O processo será repetido 1 vez.\n")

match tela:
    case '1':
        print('Usando monitor do notebook com outro monitor conectado\n')
        sleep(2)
        btCriarEntradaX = 1448
        btCriarEntradaY = 476
        btSalvarEnviarX = 287
        btSalvarEnviarY = 289
        btFecharDialogX = 1705
        btFecharDialogY = 247
        btVoltarX = 222
        btVoltarY = 188
        hrInicialX = 607
        hrInicialY = 494
    case '2':
        print('Usando monitor do notebook SEM outro monitor conectado\n')
    case _:
        print('Opção inválida, considerando monitor do notebook com outro monitor conectado)\n')
        btCriarEntradaX = 1448
        btCriarEntradaY = 476
        btSalvarEnviarX = 287
        btSalvarEnviarY = 289
        btFecharDialogX = 1705
        btFecharDialogY = 247
        btVoltarX = 222
        btVoltarY = 188
        hrInicialX = 600
        hrInicialY = 494
#verificando se o moue está na posição correta
input('Coloque o mouse sobre o botão de adicionar entrada e pressione enter\n')

#obtendo posição do mouse
xx,yy = pyautogui.position()
print(f'Posição do mouse: x={xx}, y={yy}\n')

for i in range(int(repeticaoVezes)):
    print('Indo para o navegador...\n')
    sleep(2)
    pyautogui.hotkey('alt','tab')
    sleep(1)

    #mover mouse para posição do botão de adicionar entrada
    print('Movendo para o botão de adicionar entrada...\n')
    pyautogui.moveTo(xx,yy)
    sleep(2)

    #entrando no dia
    seqFun.clickDataAddEntrada()

    # configurando zoom da pagina para 90%
    print('Configurando zoom da página para 90%...\n')
    pyautogui.hotkey('ctrl','0')
    sleep(1)
    pyautogui.hotkey('ctrl','-')
    sleep(1)

    print('Clicando no botão criar entrada de hora...\n')
    pyautogui.click(btCriarEntradaX, btCriarEntradaY)
    sleep(5)

    print('Clicando na hora inicial...')
    pyautogui.moveTo(hrInicialX, hrInicialY)

    #clicar no campo da hora inicial
    pyautogui.click()
    sleep(.7)
    pyautogui.press('tab', presses=2, interval=0.5)
    sleep(1)

    print('Verificando hora final...')
    pyautogui.hotkey('ctrl','c') #copindo valor do campo
    sleep(.7)
    #verificar valor da hora
    valorDahora = pyperclip.paste()
    if valorDahora[:2] == "12":
        pyautogui.write("12:00")
    else:
        pyautogui.write("17:00")

    print('Preenchendo o trabalho..')
    seqFun.tabAndWrite("trab", 2)

    print('Preenchendo o projeto..')
    pyautogui.press('tab') #se remover o tab debaixo, remova essa linha
    sleep(0.5)
    pyautogui.press('tab') #se remover o tab debaixo, remova essa linha
    sleep(0.5)
    pyautogui.press('tab') #se remover o tab debaixo, remova essa linha
    sleep(0.5)
    pyautogui.press('tab') #se remover o comentario da linha de baixo, remova essa linha
    sleep(0.5)
    # seqFun.tabAndWrite(seqVar.projeto, 4)
    pyperclip.copy(seqVar.projeto.encode('utf-8').decode('utf-8')) #copiando o nome do projeto
    sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    sleep(2.5)
    pyautogui.press('enter')
    sleep(1)

    print('Preenchendo o resto..')
    seqFun.tabAndWrite("100", 2,"NoENter   ")
    seqFun.tabAndWrite("sim", 1)
    seqFun.tabAndWrite("prese", 1)
    pyautogui.press('tab')
    sleep(0.7)
    pyautogui.press('tab')

    print('colando descrições..')
    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')[:195]) #copiando até qualidade
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.4)
    pyautogui.hotkey('ctrl','v')


    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')) #copiando tudo
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    sleep(0.7)

    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')[:96]) #copiando até a palavra reunião
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    sleep(0.7)

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
    # seqFun.localizarNaTela(seqVar.bt_EnviarCom2Monitores, seqVar.bt_EnviarCom2Monitores)
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
    #voltando para o terminal
    pyautogui.hotkey('alt','tab')

    #subindo o ponteiro do mouse
    yy -= 39


print('Processo finalizado!\n')
