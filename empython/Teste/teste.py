import pyautogui
import time

# Configuração de segurança: se você levar o mouse para o canto superior esquerdo, o script para.
pyautogui.FAILSAFE = True

def capturar_posicao(mensagem, delay=3):
    print(f"\n[PROMPT] {mensagem}")
    for i in range(delay, 0, -1):
        print(f"Capturando em {i}...", end="\r")
        time.sleep(1)
    x, y = pyautogui.position()
    print(f"✓ Posição capturada: {x}, {y}")
    return x, y

def main():
    acoes = [] # Lista para armazenar a sequência de passos
    
    print("--- Gravador de Automação ---")
    
    while True:
        # 1. Capturar posição de clique
        pos_clique = capturar_posicao("Posicione o mouse onde deseja CLICAR.")
        time.sleep(2)
        acoes.append({'tipo': 'clique', 'pos': pos_clique})

        # 2. Retornar ao terminal e perguntar sobre texto
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.5)
        
        decisao_texto = input("Deseja inserir algum texto neste passo? (s/n): ").strip().lower()

        if decisao_texto == 's':
            # 2.1 Capturar campo de digitação
            pos_campo = capturar_posicao("Posicione o mouse sobre o CAMPO DE DIGITAÇÃO.")
            
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            
            texto = input("Digite o texto que deseja inserir: ")
            acoes.append({'tipo': 'digitar', 'pos': pos_campo, 'conteudo': texto})
        
        # 3. Perguntar se deseja mais cliques na sequência
        mais_clique = input("\nDeseja adicionar mais um passo de clique à sequência? (s/n): ").strip().lower()
        if mais_clique != 's':
            break

    # 3.2 Definir repetições
    try:
        repeticoes = int(input("\nQuantas vezes deseja repetir toda essa sequência? "))
    except ValueError:
        repeticoes = 1

    # 4. Execução final
    print(f"\nIniciando execução em 3 segundos. Total de ciclos: {repeticoes}")
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab') # Volta para a tela alvo
    time.sleep(1)

    for acao in acoes:
        if acao['tipo'] == 'clique':
            print(f'Preparando para clicar em {acao["pos"]}...')
        elif acao['tipo'] == 'digitar':
            print(f'Preparando para digitar em {acao["pos"]}...')
            
    for i in range(repeticoes):
        print(f"Executando ciclo {i+1}/{repeticoes}...")
        for acao in acoes:
            if acao['tipo'] == 'clique':
                pyautogui.click(acao['pos'])
            elif acao['tipo'] == 'digitar':
                print(f'Clicando em {acao["pos"]}')
                pyautogui.click(acao['pos'])
                pyautogui.write(acao['conteudo'], interval=0.05) # Digita com leve intervalo
            time.sleep(2) # Pausa entre ações para estabilidade

    print("\n✓ Automação finalizada com sucesso!")

if __name__ == "__main__":
    main()