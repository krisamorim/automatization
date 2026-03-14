import random
import pyautogui
from time import sleep

pyautogui.FAILSAFE= False
pyautogui.hotkey('alt', 'tab')

#press L 3 times and wait 1 second
for i in range(400):
    pyautogui.press('l')
    print(f'{i} L pressionado')

    #se i for 100, 200, 300, wait 10 seconds
    if i == 100 or i == 200 or i == 299:
        sleep(10)

    #se i for multiplo de 100, mostrar posição do mouse
    print(f'i%100= {i%100}')
    if i % 100 == 0:
        pyautogui.moveTo(1788, 2189)
        pyautogui.click()
        x = random.randint(0, 4)
        sleep(x)
        pyautogui.write('vamoo, tap, tap, tap')
        pyautogui.press('enter')

    #clicar fora
    pyautogui.moveTo(x=1448, y=1925)
    pyautogui.click()
    sleep(2)

# #mostrar posição do mouse a cada 5 segundos
# while True:
#     sleep(5)
#     print(pyautogui.position())