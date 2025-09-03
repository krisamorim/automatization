import pyautogui
from time import sleep
import pyperclip
import dadosSensiveis as dds


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
kris_cnpj = dds.kris_cnpj
empresaKris_name = dds.empresaKris_name
cliente_cnpj =  dds.cliente_cnpj
empresaCliente_name = dds.empresaCliente_name
email_1 = dds.email_1
email_2 = dds.email_2
cnae = dds.cnae
textoincial = dds.textoincial
textDadsosbancTit = dds.textDadsosbancTit
textDadsosbanAg = dds.textDadsosbanAg
textDadsosbanCc = dds.textDadsosbanCc
valor = dds.valor


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
tabAndWrite(cliente_cnpj, 1, "NoEnter")
sleep(1)
tabAndWrite(empresaCliente_name, 1, "NoEnter")
sleep(1)
tabAndWrite(cnae, 1, "NoEnter")
sleep(1)
tabAndWrite(valor, 1, "NoEnter")
sleep(1)
pyautogui.press('tab')
sleep(1)
#titulo
pyautogui.write(textoincial)
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')

#Titulo dados bancarios
sleep(1)
pyautogui.write(textDadsosbancTit)
sleep(1)
pyautogui.press('enter')
pyautogui.write(textDadsosbanAg)
sleep(1)
pyautogui.press('enter')
pyautogui.write(textDadsosbanCc)