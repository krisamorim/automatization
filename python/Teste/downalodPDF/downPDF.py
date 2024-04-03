
import pyautogui as py
from time import sleep
i = 0
variables = {'primeiroLink': [405, 612], 'abaAtual':[851,19], 'downloadButton':[1266,149]}
for x in range(1,10):
    sleep(1)
    py.click(variables['downloadButton'])#downLoad
    sleep(1.3)
    for x in range(1,3):
        py.press(['left'])
    a = f'000{str(i)} - '
    py.write(a)
    sleep(.6)
    py.press('enter')
    sleep(1.3)
    py.hotkey('ctrl','f4')
    i+=1
    print(i)

# sleep(5)
# print(py.position())
# sleep(5)
# print(py.position())


