import pyautogui
from time import sleep
click_1_telaAOC = [359, 225] #GPT 3 pontinhos
click_2_telaAOCDELTE = [253, 318] #GPT 3 delete
click_3_telaAOCYES = [1156, 592] #GPT 3 yes

def execucao ():
    pyautogui.hotkey('alt','tab')

    for i in range(50):
        pyautogui.moveTo(click_1_telaAOC)
        sleep(.6)
        pyautogui.click(click_1_telaAOC) #3 pontos
        sleep(.6)
        pyautogui.click(click_2_telaAOCDELTE) #delet
    
        print(f'\rem execução: {i+1}/12', end='')
        sleep(.7)
    pyautogui.hotkey('alt','tab')

execucao()

# print("Esperando 3s para iniciar a execução...")
# sleep(3)
# xxx =pyautogui.position()
# print(xxx)