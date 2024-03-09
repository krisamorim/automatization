import classes as cl
from time import sleep
import openpyxl
import os
import pyautogui as pyau
import clipboard
#--------------------------------definir variaveis-------------------------
os.chdir(r'Z:\Códigos\AddUserPortalOrcamento')#linha necessária p/
pathOs = os.getcwd()
file = pathOs+'\\a.xlsx'
tempoDecarregamento = 5
workbook = openpyxl.load_workbook(file)
sheet = workbook['Validos'].iter_rows(min_row=2)
workArray = [{}]

#----Begin
cl.cls()
sleep(.7)
cl.altTab(.6)   
cl.pause('Você já está com a pagina do portal aberta e LOGADA?\n1- SIM\n2- NÃO\n>>')
# cl.checkRDS()
for linha in sheet:#criando array com Nº da loja, nome de user e cpf
    xx = []
    store = ''
    loja = str(linha[0].value)
    store = '0'+loja if len(loja) < 2 else str(loja)#tranforma numero em string e add zero nma frente se for loja de 1 a 9
    xx = {'loja':store,'Name':linha[1].va1lue, 'CPF':linha[2].value}
    workArray.append(xx)#add cada linha va variavel workArray
    cl.addUser(workArray[1]['loja'], workArray[1]['Name'],workArray[1]['CPF'])
    print(xx)
    sleep(4)

# cl.mousePosition(3)
cl.altTab(.5)
