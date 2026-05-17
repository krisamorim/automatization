import random
import pyautogui
from time import sleep

pyautogui.hotkey('alt', 'tab')
sleep(1)
historicoDevezes = []
loopDowhile = 1
while True:
    #variavel que irá definir o valor do loop
    vezes = random.randint(120, 170)
    #verificar se o valor de vezes já existe no histórico, se existir, gerar um novo valor
    while vezes in historicoDevezes:
        print(f"Valor {vezes} já existe no histórico, gerando um novo valor...")
        vezes = random.randint(120, 170)
    historicoDevezes.append(vezes)
    for i in range(vezes):
        pyautogui.press('l')
        print(f"Valor atual: {i} - Loop atual: {loopDowhile}", end='\r')
        if i % 100 == 0:
            espera = random.uniform(5, 10)
            sleep(espera)
            print(f"Esperando por {espera:.2f} segundos...")
    loopDowhile += 1
    