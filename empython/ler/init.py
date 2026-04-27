#código para ler receber um texto e ler o texto usando a voz do computador 

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Definir a velocidade da leitura
    engine.say(text)
    engine.runAndWait()
text = '''
Como você pode ver, quando imprimimos df_logs['source'].value_counts(dropna=False), o resultado é armazenado em ordem decrescente com base na contagem de cada valor. Como alternativa, podemos ordenar o resultado em ordem alfabética com base nos nomes dos valores. Para fazer isso, podemos usar o método sort_index().

import pandas as pd

df_logs = pd.read_csv('/datasets/visit_log.csv')

email_values = df_logs['email'].value_counts(dropna=True)

print(email_values)

'''
speak(text)