from time import sleep
from subprocess import Popen 
import subprocess

def cls():
    Popen(["cls"], shell=True)

def dirPopen():
    Popen(["query","session"], shell=True)

def dir():
    subprocess.run(['dir'])
    sleep(2)

def ping(destino):
    Popen(["ping", destino], shell=True)


cls()
sleep(1)
dirPopen()
# ping("www.globo.com")
# subprocess.run(["notepad.exe"])
sleep(4)

#estudar com pegar as saidas dos comandos
# p = Popen(["dir"], shell=True)
# output, erros = p.communicate()
# print(output)