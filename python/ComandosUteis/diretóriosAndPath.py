import os

os.system("cls")

print("              os.getcwd(): "+os.getcwd()) #mostra a pasta em que está nesse exato moento, não mostra a pasta do arquivo em execução, é como p PWD do linux

print("\nos.path.dirname(__file__): "+os.path.dirname(__file__)) #SOMENTE o caminho do arquivo em execuçãoa gora (sem o nome do arquivo no fina)

print("\nos.path.abspath(__file__): "+os.path.abspath(__file__)) #camiho COMPLETO (como o nome do arquivo) do arquivo em execução agora

print("")