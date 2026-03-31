#nesse código iremos utilizar pyautogui para criar uma automação que irá digitar "loja", uma espaço e depois um numero, esse numero será fornecido pelo loop, após digitar também será pressionado enter e então iremos agaurdar 1 segundo e repetir o laço
import pyautogui
from time import sleep

#Verificando quantas vezes deseja repetir o código
repeticaoVezes = input("Quantas vezes deseja repetir o processo? (Digite um número): \n")
if not repeticaoVezes.isdigit() or int(repeticaoVezes) <= 0:
    repeticaoVezes = 1
    print("Entrada inválida. O processo será repetido 1 vez.\n")


pyautogui.hotkey('alt','tab')
sleep(1)

#apertadno backspacke 15 vezes
pyautogui.press('space', presses=15, interval=0.1)
for i in range(int(repeticaoVezes)):
    #digitando "loja" + espaço + numero do loop
    texto = f'loja {i+1}'
    print(f'Digitando: {texto}\n')
    pyautogui.typewrite(texto)
    sleep(.5)
    #pressionando enter
    print('Pressionando enter...\n')
    pyautogui.press('enter')
    sleep(1)
print('Processo concluído!\n')
