import pyautogui
from time import sleep
import pyperclip


primeiroX = 410
primeiroY = 456
incre = 50

def atePrimeiraPag():
    #clicar na porcentagem de zoom
    pyautogui.moveTo(895, 147)
    pyautogui.doubleClick(895, 147)
    sleep(1)

    #ajustar % de zoom
    pyautogui.write("125")
    sleep(1)
    pyautogui.press("enter")
    sleep(1)

    #clicar no pdf
    pyautogui.doubleClick(1645, 240)
    pyautogui.press(["pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup","pgup"])
    sleep(1)
    pyautogui.press(["pgdn","pgdn","pgdn","pgdn","pgdn"])

def atualizar(primeiroX, primeiroY, increm):
    for i in range(1):
        #copiando primeiro
        print('copiando primeiro...\n')
        pyautogui.doubleClick(primeiroX,primeiroY)
        sleep(1)
        pyautogui.hotkey('ctrl','c')
        sleep(1)

        #indo p/ excel
        print('indo p/ excel...\n')
        pyautogui.hotkey('alt','tab')
        sleep(1)

        #clicar no canto superior esquerdo
        pyautogui.click(148, 444)

        pyautogui.moveTo(1644,224)
        pyautogui.click()
        sleep(2)
        pyautogui.moveTo(1675,333)
        pyautogui.click()
        sleep(2)
        pyautogui.hotkey('ctrl','v')
        sleep(1)
        pyautogui.press('enter')

print('iniciando...')
sleep(4)


# atePrimeiraPag()
atualizar(primeiroX, primeiroY, incre)
print("posicione agora o mouse")
sleep(3)
print(pyautogui.position())