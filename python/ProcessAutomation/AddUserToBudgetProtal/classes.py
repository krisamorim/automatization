from time import sleep
import pyautogui as pyau
from subprocess import Popen
import clipboard as clp


def altTab(time):
  sleep(time)
  pyau.hotkey('alt', 'tab')


def ctrlC():
  sleep(.6)
  pyau.hotkey('ctrl', 'c')
  sleep(7)


def writeWithEnter(txtInput):
  pyau.write(txtInput)
  sleep(1)
  pyau.press('enter')
  sleep(1)


def writeWithEnterWithInterval(txtInput, time):
  pyau.write(txtInput, interval=time)
  sleep(1)
  pyau.press('enter')
  sleep(1)


def cls():
  Popen('cls', shell=True)


def pause(txt):
  altTab(1)
  optiX = int(input(txt))
  if optiX == 2:
    exit()
  altTab(1)


def mousePosition(time):
  sleep(time)
  x = pyau.position()
  print(x)


def irPaginaUserDeLoja():
  pyau.click(85, 408)  #clica no sistema
  sleep(1)
  pyau.click(82, 568)  #clica no lojas
  sleep(5)


def checkIfuser():
  xx = ""
  oldPast = clp.paste()
  sleep(1)
  pyau.doubleClick(533, 220)
  sleep(.5)
  ctrlC()
  xx = clp.paste()
  return True if xx == "pertence" or xx == "pertence " else False
  clp.copy(oldPast)


def checkPageLoad(whatCheck, whatCheck2, x, y):
  oldCLipBoard = clp.paste()
  load = ''
  while load != whatCheck and load != whatCheck2:
    sleep(2)
    pyau.doubleClick(x, y)
    sleep(1)
    pyau.hotkey('ctrl', 'c')
    sleep(1)
    load = clp.paste().lstrip().rstrip()
  clp.copy(oldCLipBoard)


def validaEstabelecimento(store):
  oldCopy = clp.paste()
  clp.copy("")
  sleep(1)
  pyau.press('backspace')
  sleep(.7)
  pyau.hotkey('ctrl', 'a')
  sleep(.7)
  pyau.hotkey('ctrl', 'c')
  sleep(.6)
  cv = clp.paste().lstrip().rstrip()
  valida = True if cv[0:2] == store else False
  if valida == True:
    pyau.hotkey('ctrl', 'a')
    sleep(.07)
    print(store)
  else:
    writeWithEnter(store)
    sleep(.5)
    sleep(1)
    pyau.write(store)
    sleep(1)
    pyau.press('down')
    sleep(1)
    pyau.press('enter')
    sleep(1)
    print(cv[0:2])
    writeWithEnterWithInterval(cv[0:2], .9)
    sleep(.5)


def addUser(store, name, cpf):
  sleep(1)
  checkPageLoad('Consulta', 'Consulta', 452, 219)
  pyau.click(259, 344)  #Botão de +
  checkPageLoad('CPF', 'CPF', 433, 343)
  pyau.click(460, 348)
  sleep(.7)
  writeWithEnter(cpf)
  checkIfuserAlreadyExist = checkIfuser()

  if checkIfuserAlreadyExist == True:
    sleep(1)
    pyau.click(922, 303)  #clica no ok da mensagem
    sleep(5)
    pyau.click(469, 386)  #clica no campo de nome
    sleep(1)
    pyau.press(['tab', 'tab'])
    sleep(1)
    writeWithEnterWithInterval('sim', .8)
    sleep(.5)
    pyau.press('tab')
    sleep(1)
    validaEstabelecimento(store)
    sleep(.6)
    pyau.press('tab')
    pyau.press('space')
    writeWithEnterWithInterval('orcam', .9)
    sleep(.7)
    pyau.click(300, 207)  #save
    sleep(4)

  else:
    #get value from nome field
    pyau.click(469, 386)
    sleep(.6)
    pyau.hotkey('ctrl', 'a')
    ctrlC()
    sleep(1)
    pastValue = clp.paste()

    #check if name was autocompleted
    print('Name: {}|\nPast: {}|'.format(name, pastValue))

    if pastValue != "":
      sleep(1)
      pyau.press(['tab', 'tab'])
      sleep(1)
      writeWithEnterWithInterval('sim', .5)
      sleep(.5)
      pyau.press('tab')
      sleep(1)
      pyau.press('space')
      sleep(.6)
      writeWithEnter(store)
      pyau.press('tab')
      pyau.press('space')
      writeWithEnterWithInterval('orcam', .5)
      sleep(.7)
      pyau.click(300, 207)  #save
      sleep(4)
    else:
      pyau.click(469, 386)
      pyau.hotkey('ctrl', 'a')
      sleep(.6)
      pyau.write(name)
      sleep(1)
      pyau.press('tab')
      sleep(.7)
      pyau.write('01012005')
      sleep(1)
      writeWithEnterWithInterval('sim', .5)
      sleep(.7)
      pyau.press('tab')
      sleep(1)
      pyau.press('space')
      writeWithEnterWithInterval(store, .7)
      pyau.press('tab')
      sleep(1)
      writeWithEnterWithInterval('orcam', .5)
      sleep(.7)
      pyau.click(300, 207)  #save
      sleep(4)


def checkRDS():
  Popen(["cls"], shell=True)
  sleep(1)
  optiX = int(input('Pretende fechar o RDS?\n1-Sim\n2-Não\n'))
  if optiX == 1:
    Popen(["cls"], shell=True)
    sleep(1)
    Popen(["query", "session"], shell=True)
    sleep(1)
    print('-' * 60)
    idSession = input('Qual o id da sesão exibida acima?\n')
    Popen(["cls"], shell=True)
    sleep(1)
    print('Desconectando em 5 segundos')
    sleep(5)
    id = "rdp-tcp#" + idSession
    Popen(["tscon", id, "/dest:console"], shell=True)
    sleep(5)
    altTab(1)
