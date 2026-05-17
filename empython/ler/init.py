#código para ler receber um texto e ler o texto usando a voz do computador 

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Definir a velocidade da leitura
    engine.say(text)
    engine.runAndWait()
text = '''
Se soubermos tanto a média quanto a mediana, como devemos escolher qual usar como valor representativo? Bem, depende de qual delas é a melhor representante de um valor "típico" para o conjunto de dados.

A média não é um bom valor típico quando os dados com os quais você está trabalhando têm vários valores atípicos. Por exemplo, digamos que cinco funcionários em uma empresa têm salários de $30.000. Tanto a média como a mediana são iguais a $30.000.

Então um diretor de marketing é contratado com um salário de $90.000. A média agora aumentou para $40.000, enquanto a mediana permanece $30.000.

Esse valor atípico torna a mediana um indicador melhor do salário típico do que a média.
'''
speak(text)