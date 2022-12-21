from Util import *
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
tipos = ['fruta', 'legume', 'carne', 'limpeza', 'cereal']


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{Color.BOLD}{txt.center(42)}{Color.RESET}')
    print(linha())


def menu(titulo, lista):
    cabeçalho(titulo)
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc


def submenu(titulo, lista):
    cabeçalho(titulo)
    c = 1
    i = 0
    respostas = []
    for item in lista:
        print(f'{c} - {item}')
        if i == 0:
            respostas.append(leiaFloat('Quantia (R$): '))
            print(linha())
        elif i == 1:
            respostas.append(subOpcao(['Um carrinho', 'Dois carrinhos']))
            print(linha())
        elif i == 2:
            resposta = subOpcao(['Categoria', 'Validade em número de dias'])
            if resposta == 1:
                respostas.append(categoria())
                respostas.append('')
            elif resposta == 2:
                respostas.append('')
                respostas.append(leiaInt('Validade (dias): '))
            else:
                print(
                    f'{Color.DANGER}[Erro]: Digite uma opção válida.{Color.RESET}')
        c += 1
        i += 1
    print(linha())

    filtro = 'categoria' if respostas[3] == '' else 'validade'
    filtro_valor = respostas[2] if respostas[3] == '' else respostas[3]
    categorias = ['fruta', 'legume', 'carne', 'limpeza', 'cereal']
    filtros = {
        'dinheiro': respostas[0],
        'qtd_carrinhos': respostas[1],
        'filtro_tipo': filtro,
        'filtro_valor': categorias[filtro_valor],
    }

    return filtros


def subOpcao(lista):
    c = 1
    for item in lista:
        print(f'({c}) {item}')
        c += 1
    while True:
        opc = leiaInt('Sua opção: ')
        if(opc <= len(lista)):
            return opc
        else:
            print(
                f'{Color.DANGER}[Erro]: Digite uma opção válida.{Color.RESET}')


def categoria():
    print('Escolha a categoria:')
    c = 0
    for item in tipos:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    while True:
        opc = leiaInt('Sua opção: ')
        if(opc <= len(tipos)):
            return opc
        else:
            print(
                f'{Color.DANGER}[Erro]: Digite uma opção válida.{Color.RESET}')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                f'{Color.DANGER}[Erro]: Digite um número inteiro válido.{Color.RESET}')
            continue
        except (KeyboardInterrupt):
            print(
                f'{Color.DANGER}[Erro]: Usuário preferiu não digitar esse número.{Color.RESET}')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(
                f'{Color.DANGER}[Erro]: Formatação incorreta. Use ponto no lugar de vírgula.{Color.RESET}')
            continue
        except (KeyboardInterrupt):
            print(
                f'{Color.DANGER}[Erro]: Usuário preferiu não digitar esse número.{Color.RESET}')
            return 0
        else:
            return n


def printRecomendacao(lista):
    cabeçalho('Resumo da recomendação de compra')
    lista[0] = locale.currency(lista[0], grouping=True, symbol=None)
    if lista[3] == '':
        return print(f'Quantia: R$ {lista[0]}\n'
                     f'nº de carrinhos: {lista[1]}\n'
                     f'Categoria: {tipos[lista[2]]}')
    elif lista[2] == '':
        return print(f'Quantia: R$ {lista[0]}\n'
                     f'nº de carrinhos: {lista[1]}\n'
                     f'Validade em dias: {lista[3]}')
