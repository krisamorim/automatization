import pyautogui
from time import sleep
click_1_telaAOC = [241, 492] #GPT 3 pontinhos
click_2_telaAOCDELTE = [297, 740] #GPT 3 delete
click_3_telaAOCYES = [1156, 592] #GPT 3 yes

#clicando nos 3 pontinhos do chat
pyautogui.moveTo(click_1_telaAOC)
pyautogui.click(click_1_telaAOC)
sleep(.5)

#clicando em deletar
pyautogui.moveTo(click_2_telaAOCDELTE)
pyautogui.click(click_2_telaAOCDELTE)
sleep(.5)

#clicando em yes
pyautogui.moveTo(click_3_telaAOCYES)
pyautogui.click(click_3_telaAOCYES)
sleep(.5)

def execucao ():
    pyautogui.hotkey('alt','tab')

    for i in range(12):
        pyautogui.moveTo(240,457)
        sleep(.6)
        pyautogui.click(240,457) #3 pontos
        sleep(.6)
        pyautogui.click(242,694) #delet
        sleep(.6)
        pyautogui.click(1133,602) #yes
        print(i)
        sleep(2)
    pyautogui.hotkey('alt','tab')

# execucao()

print("Esperando 3s para iniciar a execução...")
sleep(3)
xxx =pyautogui.position()
print(xxx)