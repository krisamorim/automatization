import pandas as pd
import creden

# Lendo o arquivo CSV
try:
    df = pd.read_csv(creden.caminho_csv)
    print("Arquivo CSV lido com sucesso.")
    
    # Exibindo as primeiras linhas do arquivo
    print(df.head())

except FileNotFoundError:
    print(f"O arquivo {caminho_csv} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
