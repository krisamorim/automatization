import random
import pyautogui
from time import sleep
import random


def digitar_frases():
    # Lista de frases
    frases = [
        "vamooss",
        "vamo",
        "issu ai pessoal",
        "show de bola",
        "vamo que vamo",
        "bora pessoal",
        "excelente",
        "isso mesmo"
    ]

    # Embaralha a lista para que a ordem seja aleatória
    random.shuffle(frases)

    total_frases = len(frases)

    for indice, texto in enumerate(frases, start=1):
        print(f"Executando {indice}/{total_frases}")
        print(f"Frase: {texto}")

        # Clique na posição no icone de emotions
        pyautogui.click(1848, 2191)
        sleep(1)

        # Clique na posição do coração
        pyautogui.click(x=1867, y=1979)
        sleep(1)

        # Clique na posição da barra de texto
        pyautogui.click(x=1661, y=2192)
        sleep(1)

        # Digita a frase
        pyautogui.write(texto, interval=0.05)
        sleep(1)

        # Clique na posição de enviar
        pyautogui.click(x=1880, y=2192)

        # Tempo de espera aleatório entre 15 e 30 segundos
        esperar = random.randint(15, 30)

        print(f"Aguardando {esperar} segundos...\n")
        sleep(esperar)

    print("Todas as frases foram utilizadas sem repetição.")
#-----------------------------------------




pyautogui.hotkey('alt', 'tab')
sleep(1)
historicoDevezes = []
loopDowhile = 1
while True:
    #variavel que irá definir o valor do loop
    vezes = random.randint(120, 170)
    #verificar se o valor de vezes já existe no histórico, se existir, gerar um novo valor
    while vezes in historicoDevezes:
        print(f"Valor {vezes} já existe no histórico, gerando um novo valor...")
        vezes = random.randint(120, 170)
    historicoDevezes.append(vezes)
    for i in range(vezes):
        pyautogui.press('l')
        print(f"Valor atual: {i} - Loop atual: {loopDowhile}", end='\r')
        if i % 100 == 0:
            espera = random.uniform(5, 10)
            sleep(espera)
            print(f"Esperando por {espera:.2f} segundos...")
    loopDowhile += 1
    