from Produto import *
from Util import *
from datetime import timedelta


class Estoque:
    totalProdutos = 0
    tipos = ['fruta', 'legume', 'carne', 'limpeza', 'cereal']

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
        self.load()

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

    def getProduto(self, id):
        for tipo in self.tipos:
            if id in self.listas[tipo]:
                return [True, self.listas[tipo][id]]
            elif id == 0:
                return [False, None]

        # Caso não encontre o id em nenhuma das listas
        print(
            f"{Color.DANGER}[Erro]: O id do produto não foi encontrado.{Color.RESET}")
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

    def load(self):
        self.add(Produto("feijão", "cereal", 1.99, 2, "01/01/2023", 10))
        self.add(Produto("carne bovina", "carne", 20.0, 3, "02/01/2023", 13))
        self.add(Produto("água sanitária", "limpeza", 3.5, 3, "01/01/2024", 20))
        self.add(Produto("banana prata", "fruta", 10.58, 2, "09/01/2023", 10))
