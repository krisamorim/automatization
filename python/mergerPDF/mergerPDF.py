import PyPDF2
import os

merger = PyPDF2.PdfMerger()
# pastaAtual = os.path.dirname(__file__)
# lista_arquivos = os.listdir(pastaAtual)
pastaDosArquivos = input('Qual o caminho da pasta?\n>>')
finalNamefile = input('Qual nome vc deseja par ao arquivo final?\n>>')
lista_arquivos = os.listdir(pastaDosArquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        pathCurrentFile = pastaDosArquivos+f'\\{arquivo}'
        merger.append(pathCurrentFile)
merger.write(pastaDosArquivos+f'\\{finalNamefile}.pdf')