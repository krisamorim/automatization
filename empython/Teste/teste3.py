import pyautogui
import time


# ===== LOOP PRINCIPAL =====
for i in range(1, 30):
    pyautogui.moveTo(640,683)
    time.sleep(30)
    pyautogui.moveTo(1208,453)
    print(f"Execução {i}/30")