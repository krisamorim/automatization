import pyautogui
from time import sleep
pyautogui.FAILSAFE= False

#exibir x e y do mouse em temo real
print('Iniciando em 3 seg...')
sleep(3)
while True:
    x, y = pyautogui.position()
    print(f'Posição do mouse: x={x}, y={y}', end='\r')

1849
9911