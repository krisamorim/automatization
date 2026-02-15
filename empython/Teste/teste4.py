import pyautogui
import time
import random
import string

# ===== CONFIGURAÇÕES =====
# X = 500          # coordenada X do clique
# Y = 300          # coordenada Y do clique
TOTAL_EXECUCOES = 300
INTERVALO_CICLO = 60       # 1 minuto (em segundos)
ESPERA_APOS_CLIQUE = 5    # 5 segundos
VELOCIDADE_MOUSE = 2.5    # segundos para mover o mouse
VELOCIDADE_DIGITACAO = 0.08  # segundos entre cada tecla

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05


def gerar_texto_aleatorio(tamanho=20):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


def executar_acao():
    # Move o mouse lentamente até o ponto X,Y
    X = random.randint(790, 1501)
    Y = random.randint(1371, 2177)    
    pyautogui.moveTo(X, Y, duration=VELOCIDADE_MOUSE)
    print(f"Movido para ({X}, {Y})")

    # Clique
    pyautogui.click()
    print("Clique realizado.")
    
    # Aguarda 5 segundos
    time.sleep(ESPERA_APOS_CLIQUE)

    # Gera texto aleatório
    texto = gerar_texto_aleatorio()
    
    # Digita lentamente
    pyautogui.write(texto, interval=VELOCIDADE_DIGITACAO)
    print(f"Digitando texto: {texto}")

    pyautogui.moveTo(191, 519, duration=VELOCIDADE_MOUSE)
    

# ===== LOOP PRINCIPAL =====
for i in range(1, TOTAL_EXECUCOES + 1):
    inicio = time.time()
    print(f'Inicio {inicio}\n')
    print(f"Execução {i}/{TOTAL_EXECUCOES}")

    executar_acao()

    # Garante que o ciclo total dure 1 minuto
    tempo_gasto = time.time() - inicio
    print(f'Tempo gasto na execução: {tempo_gasto} segundos\n')

    tempo_restante = round(INTERVALO_CICLO - tempo_gasto, 2)
    print(f'Tempo restante para o próximo ciclo: {tempo_restante} segundos\n')
    if tempo_restante > 0:
        for contador in range(int(tempo_restante), 0, -1):
            print(f'Aguardando {contador} segundos...', end='\r')
            time.sleep(1)
            

print("Processo finalizado.")
