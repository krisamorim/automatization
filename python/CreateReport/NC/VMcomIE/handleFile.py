import shutil
import os
import creden
from datetime import datetime

def copyTofolderReport():
    # Construindo o caminho do arquivo de destino
    arquivo_destino = os.path.join(creden.pasta_destino, os.path.basename(creden.arquivo_origem))

    # Copiando o arquivo e sobrescrevendo se já existir
    shutil.copy2(creden.arquivo_origem, arquivo_destino)

    print(f'Arquivo copiado com sucesso para {arquivo_destino}')

def apagaSeExiste(arquivoComCaminho):
    if os.path.exists(arquivoComCaminho):
        os.remove(arquivoComCaminho)
        print(f'Arquivo {arquivoComCaminho} apagado com sucesso.')
    else:
        print(f'O arquivo {arquivoComCaminho} não existe.')

def renameAndMove(arquivo_origem, pasta_destino):
    # Obtendo o dia e o mês atual
    dia_mes = datetime.now().strftime('%d-%m')

    # Criando o novo nome para o arquivo
    novo_nome = f'{dia_mes}.csv'

    # Caminho completo do arquivo com o novo nome
    novo_caminho = os.path.join(os.path.dirname(arquivo_origem), novo_nome)

    apagaSeExiste(novo_caminho)
    
    # Renomeando o arquivo
    os.rename(arquivo_origem, novo_caminho)

    print(f'Arquivo renomeado com sucesso para {novo_caminho}')

    # Construindo o caminho do arquivo de destino
    arquivo_destino = os.path.join(pasta_destino, os.path.basename(novo_caminho))

    # Movendo o arquivo e sobrescrevendo se já existir
    shutil.move( novo_caminho, arquivo_destino)

    print(f'Arquivo movido com sucesso para {arquivo_destino}')