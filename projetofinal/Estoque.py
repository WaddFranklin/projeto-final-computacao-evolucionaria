from Produto import *
from Util import *
from datetime import timedelta


class Estoque:
    totalProdutos = 0

    def __init__(self):
        self.listaFrutas = {}
        self.listaLegumes = {}
        self.listaLimpeza = {}
        self.listaCarnes = {}
        self.listaCereais = {}
        self.listas = {
            "fruta": self.listaFrutas,
            "legume": self.listaLegumes,
            "limpeza": self.listaLimpeza,
            "carne": self.listaCarnes,
            "cereal": self.listaCereais,
        }

    def add(self, produto: Produto):
        if (produto.tipo == 'fruta'):
            self.listaFrutas[produto.id] = produto
        elif (produto.tipo == 'legume'):
            self.listaLegumes[produto.id] = produto
        elif (produto.tipo == 'limpeza'):
            self.listaLimpeza[produto.id] = produto
        elif (produto.tipo == 'carne'):
            self.listaCarnes[produto.id] = produto
        elif (produto.tipo == 'cereal'):
            self.listaCereais[produto.id] = produto
        else:
            print(
                f"{Color.DANGER}[Erro]: O produto nao eh de um tipo valido.{Color.RESET}")
            return False

        print(
            f"{Color.SUCCESS}{produto.nome} foi adicionado ao estoque com sucesso!{Color.RESET}")
        Estoque.totalProdutos += 1
        return True

    def getProduto(self, tipo, id):
        tipo = tipo.lower()
        if tipo in self.listas:
            if id in self.listas[tipo]:
                return [True, self.listas[tipo][id]]
            else:
                print(
                    f"{Color.DANGER}[Erro]: O id deste produto nao esta cadastrado no estoque.{Color.RESET}")
                return [False, None]
        else:
            print(
                f"{Color.DANGER}[Erro]: O tipo de produto nao eh valido.{Color.RESET}")
            return [False, None]

    def remove(self, tipo, id):
        existeProduto, _ = self.getProduto(tipo, id)
        if existeProduto:
            produto = self.listas[tipo].pop(id)
            print(
                f"{Color.SUCCESS}O produto {produto.nome} {produto.marca} foi removido com sucesso!{Color.RESET}")
        else:
            print(
                f"{Color.DANGER}[Erro]: O tipo de produto nao eh valido.{Color.RESET}")
            return False

        Estoque.totalProdutos -= 1
        return True

    def status(self):
        print("*** Status do Estoque ***")
        print("+------------------------------")
        print(f"| Total de produtos: {self.totalProdutos}")
        print(f"| Total de frutas: {len(self.listaFrutas)}")
        print(f"| Total de legumes: {len(self.listaLegumes)}")
        print(f"| Total de prod. limpeza: {len(self.listaLimpeza)}")
        print(f"| Total de carnes: {len(self.listaCarnes)}")
        print(f"| Total de cereais: {len(self.listaCereais)}")
        print("+------------------------------")
        print(self.listas)
