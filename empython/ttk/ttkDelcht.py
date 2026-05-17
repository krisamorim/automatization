import pyautogui
from pyttsx3 import init as init_pyttsx3
from time import sleep
#primeiro chat
click_1_telaAOC_3pontos = [359, 225] #GPT 3 pontinhos
click_2_telaAOC_DELTE = [253, 318] #GPT 3 delete


def speak(text):
    engine = init_pyttsx3()
    engine.say(text)
    engine.runAndWait()

def execucao (qntidevezes):
    pyautogui.hotkey('alt','tab')
    for i in range(qntidevezes):
        pyautogui.moveTo(click_1_telaAOC_3pontos)
        pyautogui.click(click_1_telaAOC_3pontos) #3 pontos
        sleep(.3)
        pyautogui.click(click_2_telaAOC_DELTE) #delet
        print(f'\rem execução: {i+1}/{qntidevezes}', end='')
        #veririfcar se o valor é multiplo de 10 e se for fazer sleep igual a 3 e mostrar mensegm dizendo aguaradno 3 segundos
        if (i+1) % 10 == 0 and i != qntidevezes-1:
            pyautogui.hotkey('alt','tab')
            print('\nAguardando 3 segundos...')
            speak(f'{i+1} de {qntidevezes}. Aguardando 3 segundos')
            sleep(.1)
            pyautogui.hotkey('alt','tab')
            # sleep(1)
        else:
            sleep(.6)
    pyautogui.hotkey('alt','tab')

def validarJanela():

    speak("Responda")
    #pergunta se a janela do tiktok está no monitor aoc. 1 para sim e 2 para não se for sim segue o fluxo se for não fica em loop até a pessoa dizer sim ou digitar 3 para cancelar
    resposta = input("A janela do TikTok está no monitor AOC? (1 para sim, 2 para não, 3 para cancelar): ")

    #enquanto reposta igual a 2 ou diferente de 1 ou 3 fica em loop pedindo para o usuário mover a janela do TikTok para o monitor AOC ou cancelar a execução. 
    while resposta == '2' or resposta not in ['1', '3']:
        resposta = input("Resposta inválida. Por favor, digite 1 para sim, 2 para não, ou 3 para cancelar: ")  
    if resposta == '1':
        print("Iniciando execução...")
    elif resposta == '2':
        print("Por favor, mova a janela do TikTok para o monitor AOC e execute o programa novamente.")
    elif resposta == '3':
        print("Execução cancelada pelo usuário.")
        exit()

amunetarYquantidade = 1
#perguntar qual o numero do chat em que se que iniciar. Se for 1 não fazer nada. Se for 2 em diante, subtrarir o valro do input pela variavel amunetarYquantidade e multiplicar por 75 e somar o resultado a coordenada Y dos clicks.
speak("Aguardando input")
chat_inicial = int(input("\nDigite o número do chat em que deseja iniciar (1 para o primeiro chat, 2 para o segundo, etc.): "))
if chat_inicial > 1:
    amunetarYquantidade = chat_inicial - 1
    amunetarY = amunetarYquantidade * 75
    click_1_telaAOC_3pontos[1] += amunetarY
    click_2_telaAOC_DELTE[1] += amunetarY

validarJanela()
speak("\raguaradndo input")
vezesExec = int(input("\nDigite a quantidade de vezes que deseja executar: "))
execucao(vezesExec)

# print("Esperando 3s para iniciar a execução...")
# sleep(3)
# xxx =pyautogui.position()
# print(xxx)