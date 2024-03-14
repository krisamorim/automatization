import funcTestAutom as fta
import variables as var 
import os
fta.cls()
fta.sleep(1)
fta.altTab(.5)
fta.sleep(1)

#Vendendo 1 cafeteira + 3 caps vendidas de uma unica vez + 2 caps vindidas separadamente
fta.loginPdv()
idAtual = ''
cenarios = var.importDadosExcel()
for cenario in cenarios:
    id = str(cenario['Id cenário']).strip()
    produto = str(cenario['Produto']).strip()
    quantidade = str(cenario['Quantidade']).strip()
    
    if idAtual=='':
        print('entrou no if')
        fta.sleep(20)
        fta.primeiroProdu(quantidade,produto)

    elif idAtual==id:        
        fta.venda(quantidade,produto)
    else:
        fta.finalizarVenda()
    idAtual = id
    
# fta.primeiroProdu('1','1033862')
# fta.venda('3','1030048')
# fta.venda('1','1030049')
# fta.venda('1','1030050')
# fta.finalizarVenda()


"""
#kit: Registar a fta.venda de somente 1 Kit no PDV
fta.primeiroProdu('1','1047802')
fta.pausa()
fta.finalizarfta.venda()
fta.sleep(1)

#Kit: Registar a fta.venda de 2 kits no PDV
fta.primeiroProdu('1','1047802')
fta.sleep(3)
fta.venda('1','1047802')
fta.pausa()
fta.finalizarfta.venda()

#Kit: 2 kits + combo1 (Compre um cafeteira e leve 3 capsulas por 3 centavos)
fta.primeiroProdu('1','1047802')
fta.sleep(3)
fta.venda('1','1033862')
fta.venda('1','1030049')
fta.venda('2','1030048')
fta.venda('1','1030050')
fta.pausa()
fta.finalizarfta.venda()

#kit: Kit + itens variados
fta.primeiroProdu('1','1047802')
fta.sleep(3)
fta.venda('1','1033862')
fta.venda('1','1001535')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 1: 1 cafeteria + 3 capsulas por 3 centavos
fta.primeiroProdu('1','1033862')
fta.venda('1','1030049')
fta.venda('1','1030048')
fta.venda('1','1030050')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 1: 1 cafeteria + 3 capsulas do mesmo código (por 1 centavo cada capsula)
fta.primeiroProdu('1','1033862')
fta.venda('3','1030049')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 1: 2 cafeteiras + 5 capsulas do mesmo código + 2 capsulas de outro código (por 1 centavo somente a sexta capsula)
fta.primeiroProdu('2','1033862')
fta.venda('5','1030049')
fta.venda('2','1030050')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 3: na compra de 3 toalhas a quarta toalha sai por 10,95
fta.primeiroProdu('1','1003730001')
fta.venda('1', '1003730001')
fta.venda('2','1003730001')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 3: Combo 3( a quarta toalha sai por 10,95) + Combo 1 (2 cafeteiras + 6 capsulas)
fta.primeiroProdu('4', '1003730001')
fta.venda('2','1033862')
fta.venda('3','1030049')
fta.venda('3','1030050')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 3: a cada 12, 3 toalhas saem com desconto (32,85)
fta.primeiroProdu('12', '1003730001')
fta.venda('12','1003730001')
duasfta.vendasNoKitNoPrimeifta.venda('12','1003730001','12','1003730001')
fta.venda('2','1003730001')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 3: a cada 24, 6 toalhas saem com desconto (65,70)
fta.primeiroProdu('24', '1003730001')
duasfta.vendasNoKitNoPrimeifta.venda('24','1003730001','4','1003730001')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 4: (compre 1 cadeira e ganhe 10% de desconto)
fta.primeiroProdu('1', '1001535')
duasfta.vendasNoKitNoPrimeifta.venda('2','1001535','3','1001535')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 4: (compre 1 cadeira e ganhe 10% de desconto) + Combo 1 ( 1 cafeteria + 3 capsulas por 1 centavo cada)
fta.primeiroProdu('1', '1001535')
duasfta.vendasNoKitNoPrimeifta.venda('2','1033862','4','1030051')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Registrar fta.venda COMBO 4: compre 1 cadeira e ganhe 10% de desconto (limite de 12 cadeiras com desconto)
fta.primeiroProdu('1', '1001535')
duasfta.vendasNoKitNoPrimeifta.venda('6','1001535','5','1001535')
fta.venda('1','1001535')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 5: compre 3 abridores e ganhe 10% de desconto em todos
fta.primeiroProdu('1', '1036721')
fta.venda('1','1036721')
fta.venda('1','1036721')
fta.venda('2','1036721')
fta.venda('1','1036721')
fta.pausa()
fta.finalizarfta.venda()  

#Combo: Realizar fta.venda COMBO 5: Combo 5 (compre 3 abridores e ganhe 10% de desconto em todos) + kit
fta.primeiroProdu('6', '1036721')
fta.venda('6','1036721')
fta.venda('1','1047802')
fta.pausa()
fta.finalizarfta.venda() 

#Combo: Realizar fta.venda COMBO 6: compre 2 organizadores por 69,90 (onde o 1º sairá por 59,90 e o 2º por 10,00)
fta.primeiroProdu('1', '1024088')
duasfta.vendasNoKitNoPrimeifta.venda('1','1024088','2','1024088')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 6: compre 2 organizadores por 69,90 (a cada 6 organidores 3 saem por 10,00 cada)limite de 12 organizadores com desconto
fta.primeiroProdu('6', '1024088')
duasfta.vendasNoKitNoPrimeifta.venda('6','1024088','6','1024088')
duasfta.vendasNoKitNoPrimeifta.venda('6','1024088','2','1024088')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 6: Combo 6 (compre 2 organizadores por 69,90) + Combo 5 (compre 3 abridores e ganhe 10% de desconto em todos)
fta.primeiroProdu('1', '1024088')
duasfta.vendasNoKitNoPrimeifta.venda('1','1024088','3','1036721')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 7: compre 1 furadeira e ganhe desconto na maleta
fta.primeiroProdu('2', '1040893')
fta.venda('1','1041414')
fta.venda('1','1041414')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 7: kit + Combo 7 (compre 1 furadeira e ganhe desconto na maleta)
fta.primeiroProdu('1', '1047802')
duasfta.vendasNoKitNoPrimeifta.venda('1','1040893','2','1041414')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 7: itens variados + kit + Combo 7 (compre 1 furadeira e ganhe desconto na maleta)
fta.primeiroProdu('3', '1000333')
duasfta.vendasNoKitNoPrimeifta.venda('1','1041302','1','1032020')
fta.venda('1','1047802')
fta.sleep(3)
duasfta.vendasNoKitNoPrimeifta.venda('2','1040893','2','1041414')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 8:para cada 2 canetinhas + 2 lápis o papel A4 sai com 20% de desconto 
fta.primeiroProdu('2', '1002281')
duasfta.vendasNoKitNoPrimeifta.venda('2','1011199','1','1032914')
duasfta.vendasNoKitNoPrimeifta.venda('2','1002281','2','1011199')
fta.venda('1','1032914')
fta.pausa()
fta.finalizarfta.venda()

#Combo: Realizar fta.venda COMBO 8: Combo 8 (para cada 2 canetinhas + 2 lápis o papel A4 sai com 20% de desconto) + Combo 1 (1 cafeteira + 3 capsulas por 1 centavo cada) 
fta.primeiroProdu('6', '1002281')
duasfta.vendasNoKitNoPrimeifta.venda('6','1011199','4','1032914')
duasfta.vendasNoKitNoPrimeifta.venda('1','1033862','2','1036665')
fta.venda('1','1030050')
fta.pausa()
fta.finalizarfta.venda()

#Vender um item
fta.primeiroProdu('1', '1035563')
fta.pausa()
fta.finalizarfta.venda()

#Vender dois itens
fta.primeiroProdu('1', '1035563')
fta.venda('1','1002945')
fta.pausa()
fta.finalizarfta.venda()

#ATO: Testando somente produtos que sofrem ação do ATO
fta.primeiroProdu('1', '1043870')
fta.venda('1','1041948')
fta.venda('1','1035807')
fta.venda('1','1023463')
fta.venda('1','1046286')
fta.pausa()
fta.finalizarfta.venda()

"""
#2 Kits + Combo + Orçamento
#2 Kits + 2 Combos + vale troca
#Devolver fta.venda Criada no PDV e gerar Vale Trocas
#Devolver o combo 1
#Vender itens de tributações variadas
#No PDV utilizar um vale-troca parciamente 
#Realizar fta.venda no PDV e utilizar contra vale
#No PDV utilizar um contra vale total
#Vender itens de tributações variadas
#Realizar uma fta.venda somente com orçamento
#fta.venda Combo + Orçamento
#fta.venda Kit + Orçamento
#fta.venda Kit + Combo + Orçamento
#fta.venda Kit + Combo + Orçamento (gerar VT)
#fta.venda Kit + Combo + Orçamento (pagar com VT)
#fta.venda Kit + Combo + Orçamento (gerar CV)
#fta.venda Kit + Combo + Orçamento (pagar c/ CV)

#Vender dois itens com CPF




"""
# 4 canetinhas + 2 lápis + 2 lápis, apenas 1 papel A4 
fta.primeiroProdu('2','1002281') #2 canetas
fta.venda('2','1011199') #2 lapis
fta.venda('2','1032914') #2 resmas A4 
fta.pausa()
fta.venda('2','1002281') #2 canetas
fta.venda('2','1011199') #2 lapis
fta.sleep(5)
fta.venda('1','1032914') #Resma A4
fta.sleep(5)
fta.venda('4','1002281') #2 canetas
fta.venda('4','1011199') #2 lapis
fta.venda('2','1032914') #Resma A4
fta.venda('1','1032914') #Resma A4
fta.sleep(5)
fta.finalizarfta.venda()

#teste combo 3 (toalha)
fta.primeiroProdu('4','1003730001')
fta.venda('1','1003730001')
fta.venda('1','1003730001')
fta.venda('1','1003730001')
fta.venda('1','1003730001')
fta.venda('3','1003730001')
fta.venda('1','1003730001')1
1033862

fta.venda('7','1003730001')
fta.venda('1','1003730001')
fta.sleep(8)
fta.finalizarfta.venda()

#Vendido 2 cafeteiras + 3 caps vendidas 1 a 1 + 3 caps vendidas de umaunica vez + 1 capsula
fta.primeiroProdu('2','1033862')
fta.venda('1','1030048')
fta.venda('1','1030049')
fta.venda('1','1030050')
fta.venda('3','1030050')
fta.venda('1','1030050')
fta.finalizarfta.venda()

#Vendido 1 cafeteira + 3 caps vendidas 1 a 1
fta.primeiroProdu('1','1033862')
fta.venda('1','1030048')
fta.venda('1','1030049')
f1
1033862
1ta.venda('1','1030050')
fta.finalizarfta.venda()
"""
