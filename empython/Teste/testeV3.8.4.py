from time import sleep
"""def funcionamento(variavel):
    switch_case = {
        condição1: código_para_caso1,
        condição2: código_para_caso2,
        condição3: código_para_caso3,
        # ...
        default: código_para_default,
    }
"""
def pausa():
    optiX = int(input('1- Continuar\n2- pausa\n'))
    if optiX == 2:
        exit()

print("Código executando linha 12")
sleep(2)
print("Código executando linha 14")
pausa()
print("código executando linha 16")