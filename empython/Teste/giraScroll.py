import pyautogui
import time

pyautogui.FAILSAFE = True  # Move o mouse para o canto superior esquerdo para interromper o script

pyautogui.hotkey('alt', 'tab')
time.sleep(1)  # Aguarda 1 segundo para garantir que a janela esteja ativa

INTERVALO = 60  # segundos

print("Iniciando...")
print("Pressione Ctrl+C para interromper.")

try:
    while True:
        pyautogui.press('down')
        print(f"Seta para baixo executada às {time.strftime('%H:%M:%S')}")
        time.sleep(INTERVALO)
except KeyboardInterrupt:
    print("\nPrograma encerrado.")

