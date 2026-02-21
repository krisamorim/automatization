import pyautogui
from time import sleep

print("Iniciando programa em 2 seg...")
sleep(2)

while True:
    # clicando em 3 pontinhos (X: 1316 Y: 1221)
    pyautogui.moveTo(1316, 1221, duration=0.5)
    pyautogui.click()
    sleep(.8)

    #clicando em excluir (X: 1249 Y: 1467)
    pyautogui.moveTo(1249, 1467, duration=0.5)
    pyautogui.click()

    print("Aguardando 2 segundos para finalizar...")
    sleep(2)

# pyautogui.FAILSAFE = True
# print("Mostrando posição do mouse. Pressione Ctrl-C para parar.")
# try:
#     while True:
#         x, y = pyautogui.position()
#         position_str = f'X: {x} Y: {y}'
#         print(position_str, end='')
#         print('\b' * len(position_str), end='', flush=True)
#         sleep(5)
# except KeyboardInterrupt:
#     print("\nPrograma interrompido pelo usuário.")
