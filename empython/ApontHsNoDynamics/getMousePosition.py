import pyautogui
from time import sleep

xx = 600
yy = 2050
pyautogui.moveTo(xx,yy)
sleep(2)
x,y = pyautogui.position()
for i in range(10):
    sleep(1)
    print(f'Movendo para {x}, {y} em {6 - i} segundos...')
    pyautogui.moveTo(x,y, duration=0.5)
    y -= 39

# while True:
#     question = input('Deseja continuar? (s/n): ').strip().lower()
#     if question == 's':
#         print('Dando 3 segundos para você posicionar o mouse na tela desejada...')
#         sleep(3)
#         # x, y = pyautogui.position()
#         # print(f'Posição do mouse: x={x}, y={y}')
#         print(pyautogui.position())
#     elif question == 'n':
#         break
#     else:
#         print('Resposta inválida. Por favor, responda com "s" ou "n".')
