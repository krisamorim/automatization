import os

class Cliente:
	def __init__(self, nome, email, plano):
		self.nome = nome
		self.email = email
		lista_planos = ["basic", "premium"]
		if plano in lista_planos:
			self.plano = plano
		else:
			raise Exception("Plano inválido")
		
cliente = Cliente("Lira", "lira@gmail.com", "basic")
print(cliente.nome)