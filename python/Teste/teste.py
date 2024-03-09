import pyautogui
from time import sleep
pyautogui.FAILSAFE= False
from subprocess import Popen
import testeClass as tc
import os



files = ['excelTitlebar.png','excelFunctionTitle.png','excelCopy.png']
print(len(files))

# os.chdir('.\Millium')
# files = ['excelTitlebar.png','excelFunctionTitle.png','excelCopy.png']
# file = os.path.abspath(files[0])
# executar = 1

# def pause(txt):
#   pyautogui.hotkey('alt','tab')
#   optiX = int(input(txt))
#   if optiX == 2:
#     exit()
#   pyautogui.hotkey('alt','tab')
#   sleep(.5)

# def locateOnScreenFunc(file, tentativas, timeToWaiting):
#     contador=0
#     status = False
#     while contador < tentativas:
#         try:
#             location = pyautogui.locateOnScreen(file)
#             print(f'image {file} found!')
#         except pyautogui.ImageNotFoundException:
#             print(f'Image {file} not found')
#             location = False
#         print(f'Valor de location na tentativa nº {contador}: {location}')
#         if location != False:
#             contador = tentativas
#             status = True
#             pyautogui.moveTo(location, duration=.5)
#         contador+=1
#         sleep(timeToWaiting)
#     return status

#         # search = pyautogui.locateCenterOnScreen(path)
#         # if search != None:
#         # 
#         # if search != None:
#         #     print(f'Imagem localizada em {search}')
#         #     pyautogui.moveTo(search, duration=.2)
#         #     pyautogui.click()

#         # if contador>=tentativas:
#         #     print(f'Tentativa nº {contador} sem sucesso')
#         # sleep(.25)

# while executar == 1:
#     Popen(["cls"], shell=True)
#     sleep(.5)
#     if locateOnScreenFunc(files[0], 2, 1) == False:
#         if locateOnScreenFunc(files[1], 3, 2) == False:
#             if locateOnScreenFunc(files[2], 3, 3) == False:
#                 pause('Digite 1 p/ continuar ou 2 p/ sair\n>> ')
#             else:
#                 executar = 2
                
# p1 = Popen(["md", "a"], shell=True)
# p1.wait()
# if p1.returncode == 0:
#     print('succes')
# else:
#     print('error')
# sleep(2)
# tc.altTab(1)
# sleep(3)
# tc.posicaoMouse()
# tc.pausa('1- Continuar\n2- pausa\n')