import pyautogui
from time import sleep
import pyperclip

# #mostrar posição do mouse na tela
# def mostrarPosicaoMouse():
#     while True:
#         x, y = pyautogui.position()
#         print(f'Posição do mouse: x={x}, y={y}', end='\r')
#         sleep(0.1)

# mostrarPosicaoMouse()

pyautogui.doubleClick(224,1512)

#ctrl + c
pyautogui.hotkey('ctrl','c')
sleep(1)

#salvar valo do clipboard na variavel clipbCtrlV
clipbCtrlV = pyperclip.paste()
print(f'Valor do clipboard: {clipbCtrlV}')

#se valor de clipbCtrlV diferente "Status " então aguardar 3 segundos e repetir o processo se o valor for igual a "Status " então clicar na posição 224,1512
while clipbCtrlV != "Status ":
    print('Valor do clipboard diferente de "Status ", aguardando 2 segundos...')
    sleep(2)
    pyautogui.doubleClick(224,1512)
    sleep(1)
    pyautogui.hotkey('ctrl','c')
    sleep(1)
    clipbCtrlV = pyperclip.paste()
    print(f'Valor do clipboard: {clipbCtrlV}')