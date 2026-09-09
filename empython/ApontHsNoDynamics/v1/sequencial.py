import pyautogui
from time import sleep
import pyperclip
import sequencialFuncoes as seqFun
import sequencialVariables as seqVar

print('Iniciando em 3 seg...')
sleep(3)
pyautogui.FAILSAFE = False

#Questionamento sobre nome do projeto
input(f'Mudou o nome do projeto? ele está como |{seqVar.projeto}|\n')
#Questionamento sobre carregamento das telas
input('Entre nos dialogs para carregar as telas primeiro. Depois retorne aqui e press enter\n')
#Questionamento sobre a tela
tela = input(f'Qual tela está usando?\n1-Monitor do notebook com tela externa conectada\n2-Tela do notebook SEM tela externa conectada\n3-Tela de 65"\n4-Definir pontos\n')
#Verificando quantas vezes deseja repetir o código
repeticaoVezes = input("Quantas vezes deseja repetir o processo? (Digite um número): \n")
if not repeticaoVezes.isdigit() or int(repeticaoVezes) <= 0:
    repeticaoVezes = 1
    print("Entrada inválida. O processo será repetido 1 vez.\n")

match tela:
    case '1':
        print('Usando monitor do notebook com outro monitor conectado\n')
        sleep(1)
        btCriarEntradaX = 1430
        btCriarEntradaY = 1557
        btSalvarEnviarX = 290
        btSalvarEnviarY = 1378
        btFecharDialogX = 1705
        btFecharDialogY = 1325
        btVoltarX = 218
        btVoltarY = 1274
        hrInicialX = 591
        hrInicialY = 1572
    case '2':
        print('Usando monitor do notebook SEM outro monitor conectado\n')
    case '3':
        print('Usando monitor de 65"\n')
        sleep(2)
        btCriarEntradaX = 3094
        btCriarEntradaY = 737
        btSalvarEnviarX = 555
        btSalvarEnviarY = 582
        btFecharDialogX = 3643
        btFecharDialogY = 472
        btVoltarX = 431
        btVoltarY = 385
        hrInicialX = 1248
        hrInicialY = 960
        txt2confirmPositionOKPreHora = 'Linhas'
        txt2confirmPositionOKPreHoraX = 479
        txt2confirmPositionOKPreHoraY = 1177
        txt2CheckBtnEnviarDisponivel = 'qualidade'
        txt2CheckBtnEnviarDisponivelX = 2944
        txt2CheckBtnEnviarDisponivelY = 468
        proxSalto = 81
    case '4':
        print('Definindo pontos manualmente\n')
        
        #calcular espaço entre os botões
        input('Coloque o mouse sobre o 1º botão e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        xx,yy = pyautogui.position()
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o 2º botão e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        xx2,yy2 = pyautogui.position()
        proxSalto = abs(yy2 - yy)
        print(f'y1:{yy} - y2:{yy2} = {proxSalto}\n')

        #capturar posição da barra de rolagem da tela do botão "+ Criar Entrada de Hora"
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre a barra de rolagem da tela do botão "+ Criar Entrada de Hora" e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        btBarraDeRolagemX,btBarraDeRolagemY = pyautogui.position()
        print(f'Barra de rolagem x:{btBarraDeRolagemX}  y:{btBarraDeRolagemY}\n')

        #capturar posição do botão "+ entrada"
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre "+ Criar Entrada de Hora" e press enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        btCriarEntradaX,btCriarEntradaY = pyautogui.position()
        print(f'Botão "+ Criar Entrada de Hora" x:{btCriarEntradaX}  y:{btCriarEntradaY}\n')
              
        #capturar posição do campo da hora inicial
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o campo da hr inicial e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        hrInicialX,hrInicialY = pyautogui.position()
        print(f'Posição do campo da hr inicial x:{hrInicialX}  y:{hrInicialY}\n')

        #capturar posição do botão salvar enviar
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o botão salvar/enviar e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        btSalvarEnviarX,btSalvarEnviarY = pyautogui.position()
        print(f'Posição do botão salvar enviar x:{btSalvarEnviarX}  y:{btSalvarEnviarY}\n')

        #capturar posição do texto a ser validado se o botão enviar está liberado
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o texto a ser validado se o botão enviar está liberado e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        txt2CheckBtnEnviarDisponivelX,txt2CheckBtnEnviarDisponivelY = pyautogui.position()
        print(f'Posição do texto a ser validado se o botão enviar está liberado x:{txt2CheckBtnEnviarDisponivelX}  y:{txt2CheckBtnEnviarDisponivelY}\n')
        
        txt2CheckBtnEnviarDisponivel = 'qualidade'
      
        #capturar posição do botão fechar
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o botão fechar e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        btFecharDialogX,btFecharDialogY = pyautogui.position()
        print(f'Posição do botão fechar x:{btFecharDialogX}  y:{btFecharDialogY}\n')

        #capturar posição do botão voltar
        pyautogui.hotkey('alt','tab')
        input('Coloque o mouse sobre o botão voltar e pressione enter\n')
        pyautogui.hotkey('alt','tab')
        sleep(0.7)
        btVoltarX,btVoltarY = pyautogui.position()
        print(f'Posição do botão voltar x:{btVoltarX}  y:{btVoltarY}\n')

        
        txt2confirmPositionOKPreHora = 'Linhas'

    case _:
        print('Opção inválida, considerando monitor do notebook com outro monitor conectado)\n')
        btCriarEntradaX = 1430
        btCriarEntradaY = 1557
        btSalvarEnviarX = 290
        btSalvarEnviarY = 1378
        btFecharDialogX = 1705
        btFecharDialogY = 1325
        btVoltarX = 218
        btVoltarY = 1274
        hrInicialX = 591
        hrInicialY = 1572
        txt2confirmPositionOKPreHora = 'Status '
        txt2confirmPositionOKPreHoraX = 224
        txt2confirmPositionOKPreHoraY = 1512
        txt2CheckBtnEnviarDisponivel = 'qualidade'
        txt2CheckBtnEnviarDisponivelX = 1462
        txt2CheckBtnEnviarDisponivelY = 1328
        proxSalto = 39
#se tela for diferente de 4 
if tela != '4':
    #verificando se o mouse está na posição correta
    input('Coloque o mouse sobre o botão de adicionar entrada e pressione enter\n')
    
    #obtendo posição do mouse
    xx,yy = pyautogui.position()
    print(f'Posição do mouse: x={xx}, y={yy}\n')

print('Indo para o navegador...\n')
pyautogui.hotkey('alt','tab')
sleep(.7)
if tela != '4':
    # configurando zoom da pagina para 90%
    pyautogui.click(xx,yy) #clicando para garantir que a janela está ativa
    sleep(.6)
    print('Configurando zoom da página para 90%...\n')
    pyautogui.hotkey('ctrl','0')
    sleep(.7)
    pyautogui.hotkey('ctrl','-')
    sleep(1)

for i in range(int(repeticaoVezes)):
    seqFun.speak(f'Executando {i + 1} de {repeticaoVezes}')
    #mover mouse para posição do botão de adicionar entrada
    print('Movendo para o botão de adicionar entrada...\n')
    pyautogui.moveTo(xx,yy)
    sleep(0.7)
    #Clique duplo na linha de entrada
    pyautogui.doubleClick()
    sleep(2)

    #entrando no dia
    if tela != '4':
        seqFun.clickDataAddEntrada(txt2confirmPositionOKPreHora, txt2confirmPositionOKPreHoraX, txt2confirmPositionOKPreHoraY)
    if tela == '4':
        sleep(5)
        #clicar na barra de rolagem
        pyautogui.moveTo(btBarraDeRolagemX, btBarraDeRolagemY)
        sleep(0.7)
        pyautogui.click(btBarraDeRolagemX, btBarraDeRolagemY)
        print('Clicando na barra de rolagem para garantir que a tela está carregada...\n')
        sleep(1)
    pyautogui.move(btCriarEntradaX, btCriarEntradaY)
    sleep(.6)
    print('Clicando no botão criar entrada de hora...\n')
    pyautogui.click(btCriarEntradaX, btCriarEntradaY)
    sleep(4)

    print('Clicando na hora inicial...')
    pyautogui.moveTo(hrInicialX, hrInicialY)
    sleep(1)
    #clicar no campo da hora inicial
    pyautogui.click()
    sleep(.5)
    pyautogui.press('tab', presses=2, interval=0.5)
    sleep(.6)

    print('Verificando hora final...')
    pyautogui.hotkey('ctrl','c') #copiando valor do campo
    sleep(.5)
    #verificar valor da hora
    valorDahora = pyperclip.paste()
    if valorDahora[:2] == "12":
        pyautogui.write("12:00")
    else:
        pyautogui.write("17:00")

    print('Preenchendo o projeto..')
    seqFun.tabAndWrite(seqVar.projeto, 5)
    sleep(0.5)
    
    print('Preenchendo o Percentual ..')
    seqFun.tabAndWrite("100", 2,"NoENter")
    
    print('Preenchendo o tipo trabalho..')
    seqFun.tabAndWrite("trab", 1)

    print('Preenchendo o Reserva  ..')
    seqFun.tabAndWrite("sim", 1)
    
    print('Preenchendo o local presencial  ..')
    seqFun.tabAndWrite("prese", 1)
    
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.7)
    pyautogui.press('tab')

    print('colando descrições..')
    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')[:195]) #copiando até qualidade
    sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    sleep(0.7)
    pyautogui.press('tab')

    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')) #copiando tudo
    sleep(0.4)
    pyautogui.hotkey('ctrl','v')
    sleep(0.7)
    pyautogui.press('tab')
    sleep(0.4)

    pyperclip.copy(seqVar.descr.encode('utf-8').decode('utf-8')[:96]) #copiando até a palavra reunião
    sleep(0.7)
    pyautogui.hotkey('ctrl','v')
    sleep(0.7)

    print('Buscando salvar na tela..')
    pyautogui.moveTo(btSalvarEnviarX, btSalvarEnviarY) #move o mouse para o botão salvar
    pyautogui.click(btSalvarEnviarX, btSalvarEnviarY) #clica no botão salvar
    sleep(2)
    seqFun.verificarTelaLiberada(txt2CheckBtnEnviarDisponivel, txt2CheckBtnEnviarDisponivelX,txt2CheckBtnEnviarDisponivelY) #verifica se a tela está liberada para clicar em enviar

    print('Buscando ENVIAR na tela..')
    pyautogui.moveTo(btSalvarEnviarX, btSalvarEnviarY) #move o mouse para o botão Enviar
    pyautogui.click(btSalvarEnviarX, btSalvarEnviarY) #clica no botão Enviar
    sleep(3)
    seqFun.verificarTelaLiberada(txt2CheckBtnEnviarDisponivel, txt2CheckBtnEnviarDisponivelX,txt2CheckBtnEnviarDisponivelY) #verifica se a tela está liberada para poder fecha-la
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
    yy -= proxSalto

print('Processo finalizado!\n')
