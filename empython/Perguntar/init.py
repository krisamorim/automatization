import pyautogui
import time
import os
import platform
from pathlib import Path

# Função para limpar o terminal
def limpar_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Detectar o caminho da área de trabalho, mesmo via OneDrive
desktop_path = Path.home() / "Desktop"
if not desktop_path.exists():
    desktop_path = Path.home() / "OneDrive" / "Área de Trabalho"
if not desktop_path.exists():
    desktop_path = Path.home() / "OneDrive" / "Desktop"
if not desktop_path.exists():
    raise FileNotFoundError("Não foi possível localizar a pasta da Área de Trabalho.")

# Gerar nome de arquivo com incremento se necessário
base_filename = "arquivoFinal"
extensao = ".py"
contador = 0

while True:
    if contador == 0:
        nome_arquivo = f"{base_filename}{extensao}"
    else:
        nome_arquivo = f"{base_filename}_{contador}{extensao}"
    
    caminho_arquivo = desktop_path / nome_arquivo

    if not caminho_arquivo.exists():
        break
    contador += 1

# Criar o arquivo com os imports iniciais
with open(caminho_arquivo, "w", encoding="utf-8") as f:
    f.write("import pyautogui\n")
    f.write("from time import sleep\n\n")

def adicionar_linha(linha):
    with open(caminho_arquivo, "a", encoding="utf-8") as f:
        f.write(linha + "\n")

# Loop principal
while True:
    limpar_terminal()
    time.sleep(1)
    print("\nMenu de Ações:")
    print("0 - Duplo clique")
    print("1 - Clicar")
    print("2 - Escrever texto direto")
    print("3 - Pressionar uma tecla")
    print("4 - Pressionar uma hotkey (combinação de teclas)")
    print("5 - Digitar texto com atraso")
    print("6 - Adicionar tempo de espera (sleep)")
    print("7 - Finalizar")

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        input("Posicione o mouse na posição desejada e pressione Enter...")
        posicao = pyautogui.position()
        posicaoX, posicaoY = posicao.x, posicao.y
        adicionar_linha(f"pyautogui.doubleClick({posicaoX}, {posicaoY})")
        print(f"Comando pyautogui.doubleClick({posicaoX}, {posicaoY}) adicionado.")

    elif escolha == "1":
        input("Posicione o mouse na posição desejada e pressione Enter...")
        posicao = pyautogui.position()
        posicaoX, posicaoY = posicao.x, posicao.y
        adicionar_linha(f"pyautogui.click({posicaoX}, {posicaoY})")
        print(f"Comando pyautogui.click({posicaoX}, {posicaoY}) adicionado.")

    elif escolha == "2":
        texto = input("Digite o texto que deseja escrever: ")
        adicionar_linha(f'pyautogui.write("{texto}")')
        print("Comando de escrita adicionado.")

    elif escolha == "3":
        tecla = input("Digite a tecla que deseja pressionar (ex: 'enter', 'tab', 'space'): ")
        adicionar_linha(f'pyautogui.press("{tecla}")')
        print("Comando de pressionar tecla adicionado.")

    elif escolha == "4":
        teclas = input("Digite as teclas da hotkey separadas por vírgula (ex: ctrl, c): ")
        lista_teclas = [f'"{t.strip()}"' for t in teclas.split(",")]
        adicionar_linha(f"pyautogui.hotkey({', '.join(lista_teclas)})")
        print("Comando de hotkey adicionado.")

    elif escolha == "5":
        texto = input("Digite o texto que deseja digitar com atraso: ")
        adicionar_linha(f'pyautogui.write("{texto}", interval=0.1)')
        print("Comando de digitação lenta adicionado.")

    elif escolha == "6":
        try:
            tempo = float(input("Quantos segundos de espera deseja adicionar? "))
            adicionar_linha(f"sleep({tempo})")
            print(f"Comando sleep({tempo}) adicionado.")
        except ValueError:
            print("Valor inválido. Digite um número.")

    elif escolha == "7":
        print(f"\nArquivo final salvo como: {caminho_arquivo}")
        break

    else:
        print("Opção inválida. Tente novamente.")
