import pyautogui
from time import sleep
import pyperclip


#FUNÕES-----------------------------------------------------------
def tabAndWrite(txt, tabs, NoEnter=""):
    sleep(1)
    for i in range(tabs):
        pyautogui.press('tab')
    sleep(1)
    pyautogui.write(txt)
   
   #verifica se a função recebeu valor em NoEnter
    if NoEnter in (None, ''):
        sleep(2)
        pyautogui.press('enter')
        sleep(1.5)


#VARIAVEIS-----------------------------------------------------------
kris_cnpj = '57776962000154'
empresaKris_name = "KRISHNAMURTIR AMORIM FURTADO LTDA"
linx_cnpj =  "53.464.762/0001-05"
empresaLinx_name = "LINX AUTOMOTIVO LTDA"
email_1 = 'kris.a.furtado@gmail.com'
email_2 = 'krishnamurtir.f@edu.pucrs.br'
cnae = '1.03'
# texto = 'Referente à 1ª quinzena de junho (de 16/03/25 à 31/03/25) do projeto DPASCHOAL\nDADOS BANCÁRIOS PARA DEPÓSITO:\nBanco: Bradesco S.A. (237)\nAG: 2232\nCC: 71362-7'
textoincial = 'Referente à 2ª quinzena de março (de 01/06/25 à 15/06/25) do projeto DPASCHOAL'
textDadsosbancTit = 'DADOS BANCÁRIOS PARA DEPÓSITO:\nBanco: Bradesco S.A. (237)\nAG: 2232\nCC: 71362-7'
valor = "762500"


sleep(1)
pyautogui.hotkey('alt', 'tab')
sleep(1)
pyautogui.write(kris_cnpj)
sleep(1)
tabAndWrite(empresaKris_name, 1, "NoEnter")
sleep(1)
tabAndWrite(email_1, 1, "NoEnter")
sleep(1)
tabAndWrite(email_2, 1, "NoEnter")
sleep(1)
tabAndWrite(linx_cnpj, 1, "NoEnter")
sleep(1)
tabAndWrite(empresaLinx_name, 1, "NoEnter")
sleep(1)
tabAndWrite(cnae, 1, "NoEnter")
sleep(1)
tabAndWrite(valor, 1, "NoEnter")
sleep(1)
pyautogui.press('tab')
sleep(1)
#titulo)
pyautogui.write(textoincial)
pyautogui.press('enter')
sleep(1)

#Titulo dados bancarios
sleep(1)
pyautogui.write(textoincial)
sleep(1)