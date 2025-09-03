#-*- coding:utf-8 -*-
   # import os

# class Cliente:
# 	def __init__(self, nome, email, plano):
# 		self.nome = nome
# 		self.email = email
# 		lista_planos = ["basic", "premium"]
# 		if plano in lista_planos:
# 			self.plano = plano
# 		else:
# 			raise Exception("Plano inválido")
		
# cliente = Cliente("Lira", "lira@gmail.com", "basic")
# print(cliente.nome)

import pyautogui as py
from time import sleep

# nomeCliente = input('Qual o nome do cliente:\n>>')

# fileCompleto = "C:\\etiqueta.docx"
# py.hotkey('win','r')
# sleep(2)
# py.write(fileCompleto)
# sleep(1)
# py.press('enter')
# sleep(3)
# py.hotkey('ctrl','right')
# sleep(1)
# py.press('right')
# sleep(1)
# py.write(nomeCliente)

for i in range(3):
   sleep(1)
   # print(py.position())
   py.click(234,1536) #3 pontos
   sleep(2)
   py.click(273,1687) #yes
   sleep(1)
   py.click(1135,1664) #yes
   sleep(1)