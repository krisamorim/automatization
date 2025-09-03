import pyautogui
from time import sleep
import pyperclip
import os
import sys


#FUNÕES-----------------------------------------------------------
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


#VARIAVEIS-----------------------------------------------------------
projeto = 'Gerente de Projeto Linx - Projeto DPaschoal (01-15/09/2025)'
descr = "elaborar cronograma, daily, status report, comite"
bt_EnviarCom2Monitores = 'img/bt_EnviarCom2Monitores.png'
btMozila_salverCom2Monitores = 'img/btMozila_salverCom2Monitores.png'
btMozila_salverCom2Monitores2 = 'img/btMozila_salverCom2Monitores2.png'
btMozila_salverCom2Monitores3 = 'img/btMozila_salverCom2Monitores3.png'
btMozila_fecharDialog = 'img/btMozila_fecharDialog.png'
btMozila_voltarReservas = 'img/btMozila_voltarReservas.png'

print('Iniciando em 3 seg...')
sleep(3)
#Questionamento sobre a tela
input(f'Mudou o nome do projeto? ele está como |{projeto}|\n')
input('Entre nos dialogs para carregar as telas primeiro\nDepois retorne aqui e press enter\n')


print('Indo para o navegador...')
pyautogui.hotkey('alt','tab')
sleep(1)

print('Clicando na hora inicial...')
#clicar no botão criar entrada de hora
pyautogui.click()
pyautogui.press('tab')
sleep(1)
pyautogui.press('tab')
sleep(1)

print('Verificando hora final...')
#Selecionar campo
pyautogui.hotkey('ctrl','c')
sleep(1)
#verificar valor da hora
valorDahora = pyperclip.paste()
if valorDahora == "12:30":
    pyautogui.write("12:00")

print('preenchendo o resto..')
tabAndWrite("trab", 2)
tabAndWrite(projeto, 4)
tabAndWrite("100", 2,"NoENter   ")
tabAndWrite("sim", 1)
tabAndWrite("prese", 1)
pyautogui.press('tab')
sleep(0.7)
pyautogui.press('tab')

print('colando descrições..')
#Colar descrições das atividades
pyperclip.copy(descr)
sleep(0.7)
for i in range(3):
    tabAndWrite(pyperclip.paste(), 1, "NoEnter")
sleep(2)
print('Buscando salvar na tela..')
sleep(2)
localizarNaTela(btMozila_salverCom2Monitores3,btMozila_salverCom2Monitores, btMozila_salverCom2Monitores2) #Salvar
print('Buscando ENVIAR na tela..')
sleep(3)
localizarNaTela(bt_EnviarCom2Monitores, bt_EnviarCom2Monitores)
print('Buscando Fechar na tela..')
sleep(4)
localizarNaTela(btMozila_fecharDialog,btMozila_fecharDialog)
print('Buscando "Voltar" na tela..')
sleep(2)
localizarNaTela(btMozila_voltarReservas, btMozila_voltarReservas)

#salvar
print('salve')
pyautogui.hotkey('alt','tab')


    
