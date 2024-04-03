
import pyautogui as py
from time import sleep
variables = {'pdf1':[599, 910], 'proxLinkdif':45, 'abaAtual':[1385,27], 'novaAba': [1418, 28], 'doanlodButton':[1758,237]} #variable for 50" TV
# variables = {'pdf1':[405, 612], 'proxLinkdif':45, 'abaAtual':[851,19], 'novaAba': [867,16], 'doanlodButton':[1266,149]} #variables for work laptop
i = 0
pdfLink = [599, 927]#notebookEmpresa
# pdfLink = [405, 612]#notebookEmpresa
# for x in range(1,6):
#     sleep(1)
#     py.click(851,19)#clicar na aba
#     sleep(.6)
#     py.keyDown('ctrl')
#     sleep(.5)
#     if i > 3:
#         y = pdfLink[1]-3
#         py.click(pdfLink[0],y)#abrir link em nova aba
#     py.click(pdfLink[0],pdfLink[1])#abrir link em nova aba
#     py.keyUp('ctrl')
#     sleep(3)
#     py.click(867,16)#Selecionar nova aba
#     sleep(2)
#     py.click(1266,149)#downLoad
#     sleep(3)
#     py.press(['left','left','left','left','left','left','left','left'])
#     a = f'000{str(i)} - '
#     py.write(a)
#     sleep(.6)
#     py.press('enter')
#     sleep(2)
#     py.hotkey('ctrl','f4')
#     sleep(2)
#     i+=1
#     py.click(851,17)#clicar na aba
#     sleep(1)
#     py.press('down')
#     sleep(1)
#     print(i)



y = pontos['pdf1'][1]

for x in range(1,12):
    py.moveTo(pontos['pdf1'][0],y)
    sleep(2)
    y +=45
# print(pontos['pdf1'])
# sleep(5)
# print(f'capa: {py.position()}')
# sleep(5)
# print(f'indice: {py.position()}')
# sleep(5)
# print(f'Aba atual: {py.position()}')
# sleep(5)
# print(f'Nova aba: {py.position()}')
# sleep(5)
# print(f'downalod: {py.position()}')


