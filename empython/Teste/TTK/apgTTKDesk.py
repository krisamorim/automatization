import pyautogui
from time import sleep

print("Iniciando programa em 2 seg...")
sleep(2)
contador = 0

while True:
    # clicando em 3 pontinhos 
    pyautogui.moveTo(354, 1307, duration=0.5)
    pyautogui.click()
    sleep(.2)

    #clicando em excluir 
    pyautogui.moveTo(269, 1527, duration=0.5)
    pyautogui.click()

    print("Aguardando 0.2 segundos para finalizar...")
    
    contador += 1

    #Quantidade de vezes realizadas
    print(f"Quantidade de vezes realizadas: {contador}")

    #se contador igual a multiplo de 10 agaurdar 3 segundos
    if contador % 10 == 0:
        pyautogui.hotkey('alt', 'tab')
        print("Aguardando 3 segundos para continuar...")
        sleep(3)

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
