from lib.interface import *
from time import sleep
from Produto import *

while True:
    resposta = menu(['Recomendação de compra',
                    'Listar estoque', 'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
