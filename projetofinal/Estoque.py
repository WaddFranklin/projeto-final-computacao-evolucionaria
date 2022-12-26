from Produto import *
from Util import *
from lib.interface import *
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
        self.add(Produto("morango", "fruta", 8.99, 1, "10/01/2023", 8))
        self.add(Produto("manga", "fruta", 13.87, 2, "11/01/2023", 9))
        self.add(Produto("uva", "fruta", 7.5, 1, "10/01/2024", 11))
        self.add(Produto("banana prata", "fruta", 10.58, 2, "09/01/2023", 10))
        self.add(Produto("melância", "fruta", 8.35, 3, "03/01/2023", 12))
        self.add(Produto("mamão", "fruta", 11.35, 3, "03/01/2023", 23))
        self.add(Produto("abacate", "fruta", 8.99, 3, "03/01/2023", 25))
        self.add(Produto("melão", "fruta", 7.4, 5, "03/01/2023", 15))
        self.add(Produto("laranja", "fruta", 10.00, 2, "03/01/2023", 42))
        self.add(Produto("limão", "fruta", 3.45, 3, "03/01/2023", 12))

        self.add(Produto("inhame", "legume", 6.98, 4, "08/01/2023", 15))
        self.add(Produto("cebola", "legume", 5.99, 3, "06/01/2023", 25))
        self.add(Produto("beterraba", "legume", 3.90, 2, "05/01/2023", 10))
        self.add(Produto("batata inglesa", "legume", 3.99, 2, "04/01/2023", 14))
        self.add(Produto("cenoura", "legume", 4.90, 1, "03/01/2023", 11))
        self.add(Produto("carne bovina", "carne", 30.0, 3, "05/01/2023", 13))
        self.add(Produto("peito de frango", "carne", 20.0, 2, "12/01/2023", 10))
        self.add(Produto("sardinha", "carne", 12.0, 3, "02/01/2023", 12))
        self.add(Produto("coxa de frango", "carne", 18.90, 1, "03/01/2023", 17))
        self.add(Produto("salmão", "carne", 89.90, 1, "10/01/2023", 13))
        self.add(Produto("água sanitária", "limpeza", 3.5, 3, "01/01/2024", 20))
        self.add(Produto("detergente", "limpeza", 1.50, 5, "01/05/2024", 18))
        self.add(Produto("amaciante", "limpeza", 7.5, 3, "11/06/2024", 16))
        self.add(Produto("sabão em pó", "limpeza", 3.5, 7, "01/01/2024", 19))
        self.add(Produto("esponja", "limpeza", 1.5, 10, "01/01/2024", 20))
        self.add(Produto("saco de lixo", "limpeza", 10.40, 2, "03/01/2023", 11))
        self.add(Produto("desinfetante", "limpeza", 5.35, 3, "03/01/2023", 11))
        self.add(Produto("bom ar", "limpeza", 7.90, 3, "03/01/2023", 11))
        self.add(Produto("desengordurante", "limpeza",
                 15.70, 2, "03/01/2023", 11))
        self.add(Produto("lava roupas", "limpeza", 40.00, 5, "03/01/2023", 11))

        self.add(Produto("feijão", "cereal", 1.99, 2, "01/01/2023", 10))
        self.add(Produto("milho", "cereal", 5.99, 3, "12/01/2023", 7))
        self.add(Produto("arroz", "cereal", 3.90, 2, "18/01/2023", 10))
        self.add(Produto("trigo", "cereal", 3.99, 2, "22/01/2023", 8))
        self.add(Produto("aveia", "cereal", 4.90, 1, "21/01/2023", 6))
        self.add(Produto("amaranto", "cereal", 7.90, 1, "03/01/2023", 11))
        self.add(Produto("linhaça", "cereal", 11.70, 3, "03/01/2023", 11))
        self.add(Produto("quinoa", "cereal", 8.30, 2, "03/01/2023", 11))
        self.add(Produto("cevada", "cereal", 20.80, 1, "03/01/2023", 11))
        self.add(Produto("chia", "cereal", 15.00, 3, "03/01/2023", 11))
        

    def printEstoque(self, resposta):
        if resposta == 1:
            cabeçalho('Frutas')
            for produto in self.listaFrutas:
                print(self.listaFrutas[produto].printProduto())
        elif resposta == 2:
            cabeçalho('Legumes')
            for produto in self.listaLegumes:
                print(self.listaLegumes[produto].printProduto())
        elif resposta == 3:
            cabeçalho('Carnes')
            for produto in self.listaCarnes:
                print(self.listaCarnes[produto].printProduto())
        elif resposta == 4:
            cabeçalho('Produtos de Limpeza')
            for produto in self.listaLimpeza:
                print(self.listaLimpeza[produto].printProduto())  
        elif resposta == 5:
                cabeçalho('Cereais')
                for produto in self.listaCereais:
                    print(self.listaCereais[produto].printProduto())   
        elif resposta == 6:
            cabeçalho('Todos os produtos')
            for lista in self.listas:
                for produto in self.listas[lista]:
                    print(self.listas[lista][produto].printProduto())

