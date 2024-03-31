
import pyautogui as py
from time import sleep
i = 0
pdfLink = [405, 612]
for x in range(1,6):
    sleep(1)
    py.click(851,19)#clicar na aba
    sleep(.6)
    py.keyDown('ctrl')
    sleep(.5)
    if i > 3:
        y = pdfLink[1]-3
        py.click(pdfLink[0],y)#abrir link em nova aba
    py.click(pdfLink[0],pdfLink[1])#abrir link em nova aba
    py.keyUp('ctrl')
    sleep(3)
    py.click(867,16)#Selecionar nova aba
    sleep(2)
    py.click(1266,149)#downLoad
    sleep(3)
    py.press(['left','left','left','left','left','left','left','left'])
    a = f'000{str(i)} - '
    py.write(a)
    sleep(.6)
    py.press('enter')
    sleep(2)
    py.hotkey('ctrl','f4')
    sleep(2)
    i+=1
    py.click(851,17)#clicar na aba
    sleep(1)
    py.press('down')
    sleep(1)
    print(i)

# sleep(5)
# print(py.position())
# sleep(5)
# print(py.position())


