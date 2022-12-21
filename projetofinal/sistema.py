from lib.interface import *
from time import sleep
from Produto import *
from Estoque import *
from GA import *

e = Estoque()

while True:
    resposta = menu('SISTEMA DE COMPRAS NO SUPERMERCADO', ['Recomendação de compra',
                    'Listar estoque', 'Sair do sistema'])
    if resposta == 1:
        recomendacao = submenu('Recomendação de compra', [
                               'Quanto de dinheiro disponível?', 'Quantos carrinhos de compras?', 'Qual a preferência de compras?'])

        p = Population(e, recomendacao['qtd_carrinhos'], recomendacao['dinheiro'],
                       recomendacao['filtro_tipo'], recomendacao['filtro_valor'])
        p.run()
    elif resposta == 2:
        cabeçalho('Estoque')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print(f'{Color.DANGER}[Erro]: Digite uma opção válida.{Color.RESET}')
    sleep(1)
