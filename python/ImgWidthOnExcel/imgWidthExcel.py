# from time import sleep
import classes as cl
x = 0

# cl.setZoom('70')
qntSquare = int(input('Quantos quadrados pretende avançar?\n>>'))
qntSquare = qntSquare*11
cl.altTab()
while x < 1:
  cl.pause('Selecionou o item?\n1-SIM\n2-SAIR\n>>')
  cl.selectMenu('formatar','aumentarLargura',qntSquare)
  cl.pause('Continuar?\n1-SIM\n2-NÃO\n>>')
cl.mousePosition(2)
cl.altTab()

