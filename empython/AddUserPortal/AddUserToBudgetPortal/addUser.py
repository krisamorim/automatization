import classes as cl
import openpyxl
import os
from pathlib import Path as pt

#--------------------------------definir variaveis-------------------------
cl.sleep(1)
print('os.path.curdir: '+os.path.curdir)
cl.sleep(1)
print(os.path.abspath(os.path.curdir))
cl.sleep(50)
os.chdir(r'python\ProcessAutomation\AddUserToBudgetPortal')  #linha necessária p/
cl.cls()
cl.sleep(1)
print(os.path.abspath('a.xlsx'))
cl.sleep(90)
# pathOs = os.getcwd()
print(os.getcwd())
cl.sleep(3)
cl.sleep(300)
file = os.getcwd() + '\\a.xlsx'
tempoDecarregamento = 5
workbook = openpyxl.load_workbook(file)
sheet = workbook['Validos'].iter_rows(min_row=2)
workArray = [{}]

#----Begin
cl.cls()
cl.sleep(.7)
cl.altTab(.6)
cl.pause('Você já está com a pagina do portal aberta e LOGADA?\n1- SIM\n2- NÃO\n>>')
# cl.checkRDS()
for linha in sheet:  #criando array com Nº da loja, nome de user e cpf
  xx = []
  store = ''
  loja = str(linha[0].value)
  store = '0' + loja if len(loja) < 2 else str(loja)  #tranforma numero em string e add zero na frente se for loja de 1 a 9
  xx = {'loja': store, 'Name': linha[1].value, 'CPF': linha[2].value}
  workArray.append(xx)  #add cada linha va variavel workArray
  cl.addUser(workArray[1]['loja'], workArray[1]['Name'], workArray[1]['CPF'],"sim")
  print(xx)
  cl.sleep(4)

# cl.mousePosition(3)
cl.altTab(.5)
