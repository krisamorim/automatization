import pyautogui
from time import sleep

#capturar posição do mouse e mostrar em tempo real



while True:
    pyautogui.moveTo(1555,2052)
    print('esperando 5 segundos para rolar a tela para baixo...\n')
    sleep(5)
    print('rolando a tela para baixo...\n')
    pyautogui.scroll(-700)
