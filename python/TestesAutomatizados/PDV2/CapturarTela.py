from time import sleep
import pyautogui
import os

pyautogui.FAILSAFE= False
tempo = .2
caminho_arquivo = "C:\/Users\/Milium\/desktop\/1.png"


def altTab():
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')

def abrirImagem(caminho):
    sleep(.2)
    pyautogui.keyDown('win')
    sleep(tempo)
    pyautogui.press('r')
    sleep(tempo)
    pyautogui.keyUp('win')
    pyautogui.write(caminho)
    sleep(.2)
    pyautogui.press('enter')

def altF4():
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('f4')
    sleep(tempo)
    pyautogui.keyUp('alt')
    sleep(.2)

altTab()

if os.path.exists(caminho_arquivo):
    img1.save(r"C:\Users\Milium\desktop\2.png")
    abrirImagem('%userprofile%\desktop\/2.png')
else:
    img1.save(r"C:\Users\Milium\desktop\1.png")
    abrirImagem('%userprofile%\desktop\/1.png')

sleep(5)
altF4()
altTab()
