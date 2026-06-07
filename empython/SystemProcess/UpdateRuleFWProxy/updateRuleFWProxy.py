import pyautogui as pyau
from time import sleep
import boltClass as bc
import clipboard as clp
from subprocess import Popen
from subprocess import run
from os import startfile

#-----------------------Variables----------------------
pyau.FAILSAFE = False
#ATENÇÃO
#OK p/ lojas 01, 02, 03, 05, 06, 09, 21, 33 e 58
#NÃO ok p/ lojas 04, 08

stores = ['37', '62']
regrasParaAdd = ['.whatsapp.com']

#---begin
Popen(["cls"], shell=True)#cleaning screen
bc.altTab(.6)#go to passBolt page
# bc.pausa('Pagina do PassBolt está aberta e esta como primeira aba?\n1-SIM\n2-NÃO\n>>')
# sleep(.5)
# for store in stores:
#     realizado = 0
#     sleep(.5)  
#     print('Executando p/ loja {} ({} de {} lojas!)'.format(store, realizado, len(store)))
#     bc.searchStore(store)
#     bc.accesUrl()
#     bc.accessFWproxypage(store)
#     bc.saveData(store,regrasParaAdd)
#     realizado +=1
# print('finalizado')
# bc.altTab(1)
sleep(.6)
pyau.click(625,386)