import funcTestAutom as fta
import variables as var 

fta.cls()
fta.altTab(.5)
fta.sleep(.5)
fta.pyau.press('f2')
fta.sleep(1)

# fta.loginPdv()
idAtual = ''
linha = 2
cenarios = var.importDadosExcel()
for cenario in cenarios:
    id = str(cenario['Id cenário']).strip()
    produto = str(cenario['Produto']).strip()
    quantidade = str(cenario['Quantidade']).strip()
    kit = str(cenario['O que']).strip()
    kitfind = kit.upper().find('KIT') 
    aguarda = .1
    
    if kitfind > -1:
        aguarda = 5

    if idAtual=='':
        # print('entrou no if do idAtual vazio')
        fta.primeiroProdu(quantidade, produto)
        idAtual = id
        fta.sleep(aguarda)

    elif idAtual==id:
        # print('entrou no if do idAtual igual ao id da venda atual')
        fta.venda(quantidade,produto)
        fta.sleep(aguarda)
        if linha > len(cenarios):
            fta.finalizarVenda()
    else:
        # print(f'O idAtual é {idAtual}, o id da venda é {id} por isso entrou no else')
        fta.finalizarVenda()
        fta.sleep(4)
        fta.primeiroProdu(quantidade,produto)
        fta.sleep(aguarda)
        idAtual = id
    print(f'Executando venda Nº {linha-1} da linha {linha} de uma total de {len(cenarios)}')
    linha +=1
fta.altTab(.5)
