from functions import altTab

def YesNoOption(Txt):
    Choose1 = int(input(Txt))
    if Choose1 == 0:
        exit()
    return Choose1

def someOption():
    Choose1 = int(input('Option:\n 0 to EXIT\n 1 to Sr Project\n 2 to CV Project\n 3 to Budget Project\n 4 to Acquirement Project\n 5 to ADSL Project\n 6 to DRAAS Project\n 7 to Zimbra Projact\n 8 to 82 Project\n 9 to 65 Project\n10 to IP Phone Project\n>> '))
    if Choose1 == 0:
        exit()
    print(Choose1)
    return Choose1

#Verifica se opera está aberto
def checkOperaOpen():
    Choose1 = 0
    while Choose1 == 0:
        Choose1 = int(input('Opera está aberto?\n1 para Sim\n0 para Não\n>> '))
    print('-'*15)
    input('Clique no opera e depois volte aqui para o cmd e pressione enter p/ continuar:\n>>')
    altTab(1)

