import pyautogui
from time import sleep
pyautogui.FAILSAFE= False

#--------------------------------definir variaveis-------------------------
#tempo de espera entre digitações
tempoEsperaIncicio = 2
tempEsperaDigita = 1
tempoEsperaEnter = 1

#--------------------------------definir funções-------------------------
def clickNo():
    pyautogui.click(712, 451)
    sleep(2)

def altTab(tempo):
    pyautogui.keyDown('alt')
    sleep(tempo)
    pyautogui.press('tab')
    sleep(tempo)
    pyautogui.keyUp('alt')

def pausa():
    altTab(.2)
    optiX = int(input('------------------EM PAUSE----------------\n1- Continuar\n2- Sair\n'))
    altTab(.2)
    if optiX == 2:
        exit()

def primeiroProdu(quant1stprod, cod1stProdu):
    sleep(tempoEsperaIncicio)
    pyautogui.click(781, 154)
    pyautogui.write(quant1stprod)
    pyautogui.press('enter')
    sleep(tempEsperaDigita)
    pyautogui.write(cod1stProdu)
    sleep(tempoEsperaEnter)
    pyautogui.press('enter')
    sleep(tempEsperaDigita)
    clickNo()
    sleep(3)

def duasVendasNoKitNoPrimeiVenda(qntd1prod,cod1prod,qntd2prod,cod2prod):
    #digitando qntidade do 1 produto
    sleep(1)
    pyautogui.click(781, 154)
    pyautogui.write(qntd1prod)
    pyautogui.press('enter')
    sleep(0.2)
    #digitando codigo do 2 produto
    pyautogui.write(cod1prod)
    sleep(tempoEsperaEnter)
    pyautogui.press('enter')
    sleep(.2)
    #digitando qntidade do 2 produto
    sleep(1)
    pyautogui.click(781, 154)
    pyautogui.write(qntd2prod)
    pyautogui.press('enter')
    sleep(0.2)
    #digitando codigo do 2 produto
    pyautogui.write(cod2prod)
    sleep(tempoEsperaEnter)
    pyautogui.press('enter')
    sleep(.2)

def venda(qntid,prod):
    sleep(3)
    pyautogui.click(781, 154)
    pyautogui.write(qntid)
    pyautogui.press('enter')
    sleep(tempEsperaDigita)

    #digitando codigo doproduto
    pyautogui.write(prod)
    sleep(tempoEsperaEnter)
    pyautogui.press('enter')
    sleep(2)

def finalizarVenda():
    pyautogui.press('f12')
    sleep(2)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('enter')
    sleep(7)
    clickNo()

#--------------------------------EXECUTANDO-------------------------
altTab(.2)
"""
#kit: Registar a venda de somente 1 Kit no PDV
primeiroProdu('1','1047802')
pausa()
finalizarVenda()
sleep(1)

#Kit: Registar a venda de 2 kits no PDV
primeiroProdu('1','1047802')
sleep(3)
venda('1','1047802')
pausa()
finalizarVenda()

#Kit: 2 kits + combo1 (Compre um cafeteira e leve 3 capsulas por 3 centavos)
primeiroProdu('1','1047802')
sleep(3)
venda('1','1033862')
venda('1','1030049')
venda('2','1030048')
venda('1','1030050')
pausa()
finalizarVenda()

#kit: Kit + itens variados
primeiroProdu('1','1047802')
sleep(3)
venda('1','1033862')
venda('1','1001535')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 1: 1 cafeteria + 3 capsulas por 3 centavos
primeiroProdu('1','1033862')
venda('1','1030049')
venda('1','1030048')
venda('1','1030050')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 1: 1 cafeteria + 3 capsulas do mesmo código (por 1 centavo cada capsula)
primeiroProdu('1','1033862')
venda('3','1030049')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 1: 2 cafeteiras + 5 capsulas do mesmo código + 2 capsulas de outro código (por 1 centavo somente a sexta capsula)
primeiroProdu('2','1033862')
venda('5','1030049')
venda('2','1030050')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 3: na compra de 3 toalhas a quarta toalha sai por 10,95
primeiroProdu('1','1003730001')
venda('1', '1003730001')
venda('2','1003730001')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 3: Combo 3( a quarta toalha sai por 10,95) + Combo 1 (2 cafeteiras + 6 capsulas)
primeiroProdu('4', '1003730001')
venda('2','1033862')
venda('3','1030049')
venda('3','1030050')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 3: a cada 12, 3 toalhas saem com desconto (32,85)
primeiroProdu('12', '1003730001')
venda('12','1003730001')
duasVendasNoKitNoPrimeiVenda('12','1003730001','12','1003730001')
venda('2','1003730001')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 3: a cada 24, 6 toalhas saem com desconto (65,70)
primeiroProdu('24', '1003730001')
duasVendasNoKitNoPrimeiVenda('24','1003730001','4','1003730001')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 4: (compre 1 cadeira e ganhe 10% de desconto)
primeiroProdu('1', '1001535')
duasVendasNoKitNoPrimeiVenda('2','1001535','3','1001535')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 4: (compre 1 cadeira e ganhe 10% de desconto) + Combo 1 ( 1 cafeteria + 3 capsulas por 1 centavo cada)
primeiroProdu('1', '1001535')
duasVendasNoKitNoPrimeiVenda('2','1033862','4','1030051')
pausa()
finalizarVenda()

#Combo: Registrar venda COMBO 4: compre 1 cadeira e ganhe 10% de desconto (limite de 12 cadeiras com desconto)
primeiroProdu('1', '1001535')
duasVendasNoKitNoPrimeiVenda('6','1001535','5','1001535')
venda('1','1001535')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 5: compre 3 abridores e ganhe 10% de desconto em todos
primeiroProdu('1', '1036721')
venda('1','1036721')
venda('1','1036721')
venda('2','1036721')
venda('1','1036721')
pausa()
finalizarVenda()  

#Combo: Realizar venda COMBO 5: Combo 5 (compre 3 abridores e ganhe 10% de desconto em todos) + kit
primeiroProdu('6', '1036721')
venda('6','1036721')
venda('1','1047802')
pausa()
finalizarVenda() 

#Combo: Realizar venda COMBO 6: compre 2 organizadores por 69,90 (onde o 1º sairá por 59,90 e o 2º por 10,00)
primeiroProdu('1', '1024088')
duasVendasNoKitNoPrimeiVenda('1','1024088','2','1024088')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 6: compre 2 organizadores por 69,90 (a cada 6 organidores 3 saem por 10,00 cada)limite de 12 organizadores com desconto
primeiroProdu('6', '1024088')
duasVendasNoKitNoPrimeiVenda('6','1024088','6','1024088')
duasVendasNoKitNoPrimeiVenda('6','1024088','2','1024088')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 6: Combo 6 (compre 2 organizadores por 69,90) + Combo 5 (compre 3 abridores e ganhe 10% de desconto em todos)
primeiroProdu('1', '1024088')
duasVendasNoKitNoPrimeiVenda('1','1024088','3','1036721')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 7: compre 1 furadeira e ganhe desconto na maleta
primeiroProdu('2', '1040893')
venda('1','1041414')
venda('1','1041414')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 7: kit + Combo 7 (compre 1 furadeira e ganhe desconto na maleta)
primeiroProdu('1', '1047802')
duasVendasNoKitNoPrimeiVenda('1','1040893','2','1041414')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 7: itens variados + kit + Combo 7 (compre 1 furadeira e ganhe desconto na maleta)
primeiroProdu('3', '1000333')
duasVendasNoKitNoPrimeiVenda('1','1041302','1','1032020')
venda('1','1047802')
sleep(3)
duasVendasNoKitNoPrimeiVenda('2','1040893','2','1041414')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 8:para cada 2 canetinhas + 2 lápis o papel A4 sai com 20% de desconto 
primeiroProdu('2', '1002281')
duasVendasNoKitNoPrimeiVenda('2','1011199','1','1032914')
duasVendasNoKitNoPrimeiVenda('2','1002281','2','1011199')
venda('1','1032914')
pausa()
finalizarVenda()

#Combo: Realizar venda COMBO 8: Combo 8 (para cada 2 canetinhas + 2 lápis o papel A4 sai com 20% de desconto) + Combo 1 (1 cafeteira + 3 capsulas por 1 centavo cada) 
primeiroProdu('6', '1002281')
duasVendasNoKitNoPrimeiVenda('6','1011199','4','1032914')
duasVendasNoKitNoPrimeiVenda('1','1033862','2','1036665')
venda('1','1030050')
pausa()
finalizarVenda()

#Vender um item
primeiroProdu('1', '1035563')
pausa()
finalizarVenda()

#Vender dois itens
primeiroProdu('1', '1035563')
venda('1','1002945')
pausa()
finalizarVenda()

#ATO: Testando somente produtos que sofrem ação do ATO
primeiroProdu('1', '1043870')
venda('1','1041948')
venda('1','1035807')
venda('1','1023463')
venda('1','1046286')
pausa()
finalizarVenda()

"""
#2 Kits + Combo + Orçamento
#2 Kits + 2 Combos + vale troca
#Devolver venda Criada no PDV e gerar Vale Trocas
#Devolver o combo 1
#Vender itens de tributações variadas
#No PDV utilizar um vale-troca parciamente 
#Realizar venda no PDV e utilizar contra vale
#No PDV utilizar um contra vale total
#Vender itens de tributações variadas
#Realizar uma venda somente com orçamento
#Venda Combo + Orçamento
#Venda Kit + Orçamento
#Venda Kit + Combo + Orçamento
#Venda Kit + Combo + Orçamento (gerar VT)
#Venda Kit + Combo + Orçamento (pagar com VT)
#Venda Kit + Combo + Orçamento (gerar CV)
#Venda Kit + Combo + Orçamento (pagar c/ CV)

#Vender dois itens com CPF




"""
# 4 canetinhas + 2 lápis + 2 lápis, apenas 1 papel A4 
primeiroProdu('2','1002281') #2 canetas
venda('2','1011199') #2 lapis
venda('2','1032914') #2 resmas A4 
pausa()
venda('2','1002281') #2 canetas
venda('2','1011199') #2 lapis
sleep(5)
venda('1','1032914') #Resma A4
sleep(5)
venda('4','1002281') #2 canetas
venda('4','1011199') #2 lapis
venda('2','1032914') #Resma A4
venda('1','1032914') #Resma A4
sleep(5)
finalizarVenda()

#teste combo 3 (toalha)
primeiroProdu('4','1003730001')
venda('1','1003730001')
venda('1','1003730001')
venda('1','1003730001')
venda('1','1003730001')
venda('3','1003730001')
venda('1','1003730001')
venda('7','1003730001')
venda('1','1003730001')
sleep(8)
finalizarVenda()

#Vendido 2 cafeteiras + 3 caps vendidas 1 a 1 + 3 caps vendidas de umaunica vez + 1 capsula
primeiroProdu('2','1033862')
venda('1','1030048')
venda('1','1030049')
venda('1','1030050')
venda('3','1030050')
venda('1','1030050')
finalizarVenda()

#Vendido 1 cafeteira + 3 caps vendidas 1 a 1
primeiroProdu('1','1033862')
venda('1','1030048')
venda('1','1030049')
venda('1','1030050')
finalizarVenda()
"""
#Vendend 1 cafeteira + 3 caps vendidas de uma unica vez + 2 caps vindidas separadamente
primeiroProdu('1','1033862')
venda('3','1030048')
venda('1','1030049')
venda('1','1030050')
finalizarVenda()
