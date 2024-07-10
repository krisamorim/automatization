from time import sleep
import os
import pyautogui as pyau
# import clipboard as clip
from subprocess import Popen, PIPE
# import variables as vari
from datetime import datetime

# Obter a data e hora atual
data_atual = datetime.now().strftime("%Y%m%d")

def cls():
    Popen(["cls"], shell=True)
    sleep(1)

def getMousePosition(waitingTime):
    choose = 0
    while choose == 0:
        input('O que vc vai fazer: ')
        altTab(1)
        sleep(waitingTime)
        print(pyau.position())
        altTab(1)
        choose = int(input('0 para Continuar'))
        print('-'*20)

def altTab(waitingTime):
    sleep(waitingTime)
    pyau.hotkey('alt','tab')
    sleep(waitingTime)

def pause(txt):
    altTab(.7)
    optiX = int(input(txt))
    if optiX == 2:
        print('')

def downloadListOpenSprint():
    pyau.hotkey('win','r')
    sleep(1)
    pyau.write('opera')
    sleep(1)
    pyau.press('enter')
    sleep(2)
    pyau.write('https://netcredbrasil.atlassian.net/jira/software/projects/DEV/boards/6')
    sleep(1)
    pyau.press('enter')
    sleep(4)
    # pyau.click(561,1049) #clicar no opera na barra de tarefas
    # sleep(1)
    # pyau.click(192,32) #clicar na tab do jira
    # sleep(1)
    pyau.click(387,178) #clicar nos filtros
    sleep(1)
    pyau.click(488,361) #Selecionar filtro de sprint aberta
    sleep(4)
    pyau.click(1533,262) #seleciona opção exportar
    sleep(1)
    pyau.click(1441,650) #seleciona exporta em csv
    sleep(1)

def openFolder(caminho):
    sleep(1)
    pyau.hotkey('win','r')
    sleep(1)
    pyau.write(caminho)
    sleep(1)
    pyau.press('enter')

def moveFile(caminhoOrigem,camilhoFinal):
    openFolder(caminhoOrigem)
    sleep(2)
    #selecionar primeiro arquivo
    pyau.press('down')
    sleep(1)
    pyau.press('up')
    sleep(1)
    #recortar
    pyau.hotkey('ctrl','x')
    sleep(2)
    pyau.hotkey('alt','f4')
    sleep(1)
    #iniciando processo de colar
    openFolder(camilhoFinal)
    sleep(2)
    pyau.hotkey('ctrl','v')
    sleep(1)

def gotTourlWithOperaOpen(url):
    sleep(1)
    pyau.hotkey('ctrl','t')
    print('Abrindo nova aba..')
    sleep(1)
    pyau.write(url)
    print('Digitando url')
    sleep(2)
    pyau.press('enter')
    sleep(4)
    print('Esperando pagina carregar...')
    pyau.click(x=424, y=185) #clicar nos filtros
    sleep(1)
    print('Clicando no menu filtro')
    pyau.click(x=548, y=386) #Selecionar filtro de sprint aberta
    sleep(4)
    print('Selecionando filtro')
    pyau.click(x=1530, y=259) #seleciona opção exportar
    sleep(1)
    print('Exportando')
    pyau.click(x=1415, y=818) #seleciona exporta em excel csv (campos personalizados)
    sleep(4)
    print("exportação finalizada")

def moveFile():
    sleep(4)
    # Define os caminhos de origem e destino
    source_path = "C:\\Users\\krisn\\Downloads\\Prj Dev _ Sprint Open  (Jira).csv"
    destination_path = "C:\\Users\\krisn\\OneDrive\\Área de Trabalho\\NC\\Report\\"

    # Comando para mover o arquivo
    move_command = f'move /y "{source_path}" "{destination_path}"'

    # Executa o comando usando Popen
    process = Popen(
        move_command, 
        shell=True, 
        stdout=PIPE, 
        stderr=PIPE,
        text=True
    )

    # Captura a saída e possíveis erros
    stdout, stderr = process.communicate()

    # Armazena o resultado em uma variável
    resultBat = stdout.strip()

    # Verifica se há erros e armazena a mensagem de erro
    error_message = stderr.strip()

    # Exibe o resultado
    if resultBat:
        print("Comando executado com sucesso:")
        print(resultBat)
    if error_message:
        print("Erro na execução do comando:")
        print(error_message)
