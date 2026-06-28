import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()

        print(
            f"\rPosição atual do mouse -> X: {x:5d} | Y: {y:5d}",
            end="",
            flush=True
        )

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nPrograma encerrado.")

   