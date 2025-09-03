import pyautogui
from time import sleep

#Pegar posição do primeiro click em area não digitavel
input("Pressione enter e posicione o mouse na posição do primeiro click\n")
sleep(1)
pyautogui.hotkey('alt','tab')
sleep(1)
firstAreaNaodigitavelX, firstAreaNaodigitavelY = pyautogui.position() 
print(f"Mouse no 1º click: {pyautogui.position()}")
pyautogui.hotkey('alt','tab')
sleep(1)

#Pegar posição do segundo click em area digitavel
input("Pressione enter e posicione o mouse na posição do segundo click em campo digitalvel\n")
sleep(1)
pyautogui.hotkey('alt','tab')
sleep(1 )
secondAreaNaodigitavelX, secondAreaNaodigitavelY = pyautogui.position() 
print(f"Mouse no 2º click da area digital: {pyautogui.position()}")
pyautogui.hotkey('alt','tab')
sleep(1)

#iniciar script
input("Pressione enter iniciar o script\n")
pyautogui.hotkey('alt','tab')
sleep(1)

contador = 1

while True:
    #movendo para o campo de digitação e clicando
    pyautogui.moveTo(secondAreaNaodigitavelX,secondAreaNaodigitavelY)
    sleep(1)
    pyautogui.click()
    sleep(2)
    pyautogui.write("......................................................")
    sleep(1)

    #movendo para outro ponto......................................................
    pyautogui.moveTo(firstAreaNaodigitavelX,firstAreaNaodigitavelY)
    sleep(1)
    pyautogui.click()

    #movendo para o campo de digitação e clicando
    pyautogui.moveTo(secondAreaNaodigitavelX,secondAreaNaodigitavelY)
    sleep(1)
    pyautogui.click()
    sleep(2)
    pyautogui.hotkey('ctrl','a')
    sleep(2)
    pyautogui.press('backspace')
    sleep(1)

    #Mostrando contador
    pyautogui.hotkey('alt','tab')
    print(f'{contador}º execução')
    sleep(5)
    pyautogui.hotkey('alt','tab')
    sleep(1)

    contador+=1

# # Obtém a posição atual do mouse
# posicao_mouse = pyautogui.position()......................................................

# # Exibe a posição do mouse
# print(f"A posição do mouse é: {posicao_mouse}")