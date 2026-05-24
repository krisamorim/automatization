import pyautogui
from time import sleep
tresPontinhosTELANOTEBOOK = [351,1309]
deletarTELANOTEBOOK = [261,1395]
print("Iniciando programa em 2 seg...")
sleep(2)
contador = 0

while True:
    # clicando em 3 pontinhos 
    pyautogui.moveTo(tresPontinhosTELANOTEBOOK[0], tresPontinhosTELANOTEBOOK[1], duration=0.5)
    pyautogui.click()
    sleep(.2)

    #clicando em excluir 
    pyautogui.moveTo(deletarTELANOTEBOOK[0], deletarTELANOTEBOOK[1], duration=0.5)
    pyautogui.click()
    
    contador += 1

    #Quantidade de vezes realizadas
    print(f"Quantidade de vezes realizadas: {contador}", end='\r')

    #se contador igual a multiplo de 10 agaurdar 3 segundos
    if contador % 10 == 0:
        pyautogui.hotkey('alt', 'tab')
        print("Aguardando 3 segundos para continuar...")
        sleep(3)

