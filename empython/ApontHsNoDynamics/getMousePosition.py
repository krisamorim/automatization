import pyautogui
from time import sleep

while True:
    question = input('Deseja continuar? (s/n): ').strip().lower()
    if question == 's':
        print('Dando 3 segundos para você posicionar o mouse na tela desejada...')
        sleep(3)
        # x, y = pyautogui.position()
        # print(f'Posição do mouse: x={x}, y={y}')
        print(pyautogui.position())
    elif question == 'n':
        break
    else:
        print('Resposta inválida. Por favor, responda com "s" ou "n".')
