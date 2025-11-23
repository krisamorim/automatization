import pyautogui
from time import sleep
import os
import sys
import pyperclip

def clickDataAddEntrada():
    #Clique duplo no hora
    pyautogui.doubleClick()
    sleep(4)

    #Descendo toda a tela
    print('pressionando ctrl+end 3 vezes\n')
    sleep(3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('end', presses=3)
    print('aguardando 3 seg\n')
    sleep(3)
    pyautogui.press('end', presses=3)
    pyautogui.keyUp('ctrl')
    sleep(3)
    pyautogui.press('end', presses=33)
    sleep(2)
    pyautogui.press('end', presses=13)

def tabAndWrite(txt, tabs, NoEnter=""):
    sleep(0.7)
    for i in range(tabs):
        pyautogui.press('tab')
    sleep(0.7)
    pyautogui.write(txt)
   
   #verifica se a função recebeu valor em NoEnter
    if NoEnter in (None, ''):
        sleep(2)
        pyautogui.press('enter')
        sleep(1.5)

def mudarDir():
    # Caminho absoluto do arquivo atual
    caminho_arquivo = os.path.abspath(sys.argv[0])
    print(f'Caminho absoluto do arquivo é {caminho_arquivo} ')
    # Pasta onde o arquivo está
    pasta_atual = os.path.dirname(caminho_arquivo)
    print(f'\nApasta é {pasta_atual} ')
    # Mudar o diretório de trabalho
    os.chdir(pasta_atual)
    print(f"\nDiretório alterado para: {pasta_atual}")
    return pasta_atual

def verificarTelaLiberada(palavra, x, y):
    pyperclip.copy('vazio')
    print(f'valor co clipboard é {pyperclip.paste()}')
    while pyperclip.paste() != palavra:
        print('Tela não liberada, aguardando 3 segundos...')
        sleep(3)
        pyautogui.doubleClick(x,y)
        sleep(1)
        pyautogui.hotkey('ctrl','c')

# Localiza a imagem na tela
def localizarNaTela(*imagens, tentativas_maximas=3, confianca_inicial=0.5):
    mudarDir()
    sleep(1)
    for idx, imagem_alvo in enumerate(imagens):
        print(f"Tentando localizar a imagem {idx + 1}: {imagem_alvo}")
        
        # Verifica se o arquivo existe
        if not os.path.exists(imagem_alvo):
            print(f"Arquivo não encontrado: {imagem_alvo}")
            pyautogui.hotkey('alt', 'tab')
            sleep(99)
            return imagem_alvo
        
        # Tenta com diferentes níveis de confiança
        for tentativa in range(tentativas_maximas):
            try:
                # Diminui a confiança a cada tentativa
                confianca = confianca_inicial - (tentativa * 0.1)
                confianca = max(confianca, 0.2)  # Nunca menor que 0.4
                
                print(f"Tentativa {tentativa + 1} com confiança {confianca:.1f}")
                localizacao = pyautogui.locateCenterOnScreen(
                    imagem_alvo, 
                    confidence=confianca,
                    # grayscale=True  # Pode ajudar na detecção
                )
                
                if localizacao:
                    print(f"Imagem encontrada em: {localizacao}")
                    pyautogui.moveTo(localizacao)
                    sleep(0.5)
                    pyautogui.click()
                    return localizacao
                    
            except pyautogui.ImageNotFoundException:
                print(f"Imagem não encontrada na tentativa {tentativa + 1}")
                sleep(1)  # Espera entre tentativas
        
        print(f"Imagem {idx + 1} não encontrada após {tentativas_maximas} tentativas.")
    
    print("Nenhuma das imagens foi encontrada.")
    return None