import pyautogui
from time import sleep
import os
import sys
from datetime import datetime

# Espera 2 segundos para você abrir a tela desejada
sleep(2)

#------------------------------------------------------------VARIÁVEIS------------------------------------------------------------------------#
# Caminho da imagem dentro da pasta 'img'
bt_reservRecurso3 = 'img/bt_reservRecurso3.png'
bt_reservRecurso2 = 'img/bt_reservRecurso2.png'


############################################################-------FUNÇÕES--------##################################################################

def data_atual_formatada():
    return datetime.now().strftime('%d/%m/%Y')

def mudarDir():
    # Caminho absoluto do arquivo atual
    caminho_arquivo = os.path.abspath(sys.argv[0])
    print(f'Caminho absoluto do arquivo é {caminho_arquivo} ')

    # Pasta onde o arquivo está
    pasta_atual = os.path.dirname(caminho_arquivo)
    print(f'Apasta é {pasta_atual} ')

    # Mudar o diretório de trabalho
    os.chdir(pasta_atual)
    print(f"Diretório alterado para: {pasta_atual}")

    return pasta_atual

# Localiza a imagem na tela
def localizarNaTela(*imagens):

    for idx, imagem_alvo in enumerate(imagens):
        print(f"Tentando localizar a imagem {idx + 1}: {imagem_alvo}")
        mudarDir()
        sleep(1)
        # Verifica se o arquivo existe antes de tentar localizar na tela
        if os.path.exists(imagem_alvo):
            localizacao = pyautogui.locateCenterOnScreen(imagem_alvo, confidence=0.8)
            if localizacao:
                print(f"Imagem encontrada: {localizacao}")
                pyautogui.moveTo(localizacao)
            else:
                print("Imagem não encontrada na tela.")
        else:
            print(f"Arquivo não encontrado: {imagem_alvo}")
            pyautogui.hotkey('alt','tab')
            return imagem_alvo


        tentativas = 0
        while tentativas < 3:
            localizacao = pyautogui.locateCenterOnScreen(imagem_alvo, confidence=0.6)

            if localizacao:
                print(f"Imagem {idx + 1} encontrada em: {localizacao}")
                pyautogui.moveTo(localizacao)
                sleep(1)
                pyautogui.click(localizacao)
                print("Movimentação do mouse realizada.")
                return localizacao  # <- Interrompe aqui ao encontrar
            else:
                tentativas += 1
                print(f"Tentativa {tentativas} falhou para a imagem {idx + 1}.")
                sleep(1)  # Espera entre tentativas

        print(f"Imagem {idx + 1} não encontrada após 3 tentativas.")

    print("Nenhuma das imagens foi encontrada.")
    return None  # Retorna None se nenhuma imagem for localizada

print(data_atual_formatada())
sleep(90)

pyautogui.hotkey('alt','tab') #vai p/ o navegador
sleep(1)

#localizar texto na tela 
pyautogui.hotkey('ctrl','f')
sleep(1)
pyautogui.write('reservas de recur')
sleep(2)

localizarNaTela(bt_reservRecurso3, bt_reservRecurso2)

sleep(1)
pyautogui.hotkey('alt','tab')