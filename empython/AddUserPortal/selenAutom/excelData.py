import openpyxl
import os
#-------------------------------- variaveis-------------------------
# pathComplet = os.path.join(os.getcwd(),'Milium','selenAutom')
os.chdir(r'z:\codes\Millium\selenAutom')#linha necessária p/
file = 'a.xlsx'
tempoDecarregamento = 5
workbook = openpyxl.load_workbook(file) #carregar arquivo excel no progrma
sheet = workbook['Validos'].iter_rows(min_row=2) #definido a pagina do arquivo de excel e definindo para ler a aprtir da segunda linha
workArray = []

#----Begin
# cl.checkRDS()
def dados():
    for linha in sheet:#criando array com Nº da loja, nome de user e cpf
        xx = []
        store = ''
        loja = str(linha[0].value)
        store = '0'+loja if len(loja) < 2 else str(loja)#tranforma numero em string e add zero nma frente se for loja de 1 a 9
        xx = {'loja':store,'Name':linha[1].value, 'CPF':linha[2].value} #cria um objeto
        workArray.append(xx)#add o objeto criado na variavel workArray
    return workArray