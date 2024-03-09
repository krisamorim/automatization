"""
-------------------------------------COMANDOS---------------------------------
Como clicar e arrastar Pyautogui?
position()", podemos clicar nele com "pyautogui. click(x,y)" e mover com "pyautogui. moveTo(x,y)"

pegar posição mouse
x = pyautogui.position()
print(x)

Mover mouse com o o botão esquerdo pressionado
sleep(1)
pyautogui.moveTo(128, -749)
sleep(1)
pyautogui.mouseDown(button='left')
sleep(.5)
pyautogui.moveTo(499, -549)
sleep(1)
pyautogui.mouseUp(button='left')
"""