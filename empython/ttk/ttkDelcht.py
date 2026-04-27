import pyautogui
from pyttsx3 import init as init_pyttsx3
from time import sleep
click_1_telaAOC = [359, 225] #GPT 3 pontinhos
click_2_telaAOCDELTE = [253, 318] #GPT 3 delete
click_3_telaAOCYES = [1156, 592] #GPT 3 yes

def speak(text):
    engine = init_pyttsx3()
    engine.say(text)
    engine.runAndWait()

def execucao (qntidevezes):
    pyautogui.hotkey('alt','tab')
    for i in range(qntidevezes):
        pyautogui.moveTo(click_1_telaAOC)
        sleep(.3)
        pyautogui.click(click_1_telaAOC) #3 pontos

        pyautogui.click(click_2_telaAOCDELTE) #delet
    
        print(f'\rem execução: {i+1}/{qntidevezes}', end='')
        #veririfcar se o valor é multiplo de 10 e se for fazer sleep igual a 3 e mostrar mensegm dizendo aguaradno 3 segundos
        if (i+1) % 10 == 0 and i != qntidevezes-1:
            pyautogui.hotkey('alt','tab')
            print('\nAguardando 3 segundos...')
            speak(f'{i+1} de {qntidevezes}. Aguardando 3 segundos')
            sleep(2)
            pyautogui.hotkey('alt','tab')
            sleep(1)
        else:
            sleep(.6)
    pyautogui.hotkey('alt','tab')

execucao(200)

# print("Esperando 3s para iniciar a execução...")
# sleep(3)
# xxx =pyautogui.position()
# print(xxx)