import psycopg2
import pandas as pd
import creden  # Importa as variáveis de creden.py

# Função principal
def inserir_dados_no_banco():
    print('-'*20)
    print('Iniciando alimentação do banco de dados')
    try:
        # Conexão com o banco de dados
        conexao = psycopg2.connect(
            host=creden.hostIP,
            database=creden.dbName,
            user=creden.userName,
            password=creden.password
        )
        print("Conexão ao banco de dados realizada com sucesso.")

        # Criando um cursor para executar comandos
        cursor = conexao.cursor()

        # Obter os nomes e tipos das colunas da tabela, ignorando a primeira (autoincremental)
        cursor.execute(f"""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = '{creden.tableName}' 
            ORDER BY ordinal_position;
        """)
        colunas_info = cursor.fetchall()
        colunas_sem_autoincremental = colunas_info[1:]  # Ignorar a primeira coluna autoincremental
        print(f"Colunas da tabela '{creden.tableName}' (sem a autoincremental): {colunas_sem_autoincremental}")

        # Lendo o arquivo CSV
        df = pd.read_csv(creden.caminho_csv)
        print(f"Dados do arquivo CSV '{creden.caminho_csv}' lidos com sucesso.")

        # Apagando todos os dados da tabela (opções: DELETE ou TRUNCATE)
        cursor.execute(f"TRUNCATE TABLE {creden.tableName} RESTART IDENTITY;")
        conexao.commit()
        print(f"Todos os dados da tabela '{creden.tableName}' foram apagados.")

        # Mapeando os tipos de dados PostgreSQL para tipos Python
        def ajustar_valor_para_tipo(valor, tipo_dado):
            if tipo_dado in ['integer', 'bigint', 'smallint']:
                return int(valor) if pd.notna(valor) else None
            elif tipo_dado in ['numeric', 'decimal', 'real', 'double precision']:
                return float(valor) if pd.notna(valor) else None
            elif tipo_dado in ['boolean']:
                return bool(valor) if pd.notna(valor) else None
            elif tipo_dado in ['date']:
                return pd.to_datetime(valor).date() if pd.notna(valor) else None
            else:  # Trata como string para tipos como 'character varying', 'text', etc.
                return str(valor) if pd.notna(valor) else None

        # Loop para inserir os dados linha por linha
        for index, row in df.iterrows():
            valores_linha = []

            # Ajusta cada valor da linha de acordo com o tipo de dado da coluna
            for (coluna, tipo_dado), valor in zip(colunas_sem_autoincremental, row):
                valor_ajustado = ajustar_valor_para_tipo(valor, tipo_dado)
                valores_linha.append(valor_ajustado)

            # Montando o SQL dinamicamente sem a primeira coluna (autoincremental)
            values = ', '.join(['%s'] * len(valores_linha))
            insert_query = f"INSERT INTO {creden.tableName} ({', '.join([col[0] for col in colunas_sem_autoincremental])}) VALUES ({values})"

            # Executando a query de inserção
            cursor.execute(insert_query, tuple(valores_linha))

        # Commit das alterações
        conexao.commit()
        print(f"Dados inseridos com sucesso na tabela '{creden.tableName}'.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        if conexao:
            conexao.rollback()  # Faz rollback em caso de erro

    finally:
        # Fechando a conexão
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        print("Conexão ao banco de dados encerrada.")


