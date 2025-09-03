import creden
import psycopg2

# Conectando ao banco de dados
try:
    conexao = psycopg2.connect(
        host=creden.hostIP,
        database=creden.dbName,
        user=creden.userName,
        password=creden.password
    )
    print("Conexão ao banco de dados realizada com sucesso.")

   # Criando um cursor para executar comandos
    cursor = conexao.cursor()

    # Criando a consulta SQL dinamicamente usando a variável tableName
    query = f"SELECT * FROM {creden.tableName} LIMIT 0;"
    
    # Executando a consulta para obter os nomes das colunas
    cursor.execute(query)
    colunas = [desc[0] for desc in cursor.description]

    # Exibindo os nomes das colunas
    print(f"Nomes das colunas na tabela '{creden.tableName}':")
    for coluna in colunas:
        print(coluna)

except Exception as e:
    print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")

finally:
    # Fechando a conexão
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão ao banco de dados encerrada.")