import pyautogui
from time import sleep
import pyperclip

texto = "Teste de automação de NF-e"

pyperclip.copy(texto)
print(pyperclip.paste())