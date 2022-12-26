from datetime import date


class Produto:

    idProduto = 0

    def __init__(self, nome, tipo, preco, volume, data_vencimento, quantidade):
        Produto.idProduto += 1
        self.id = Produto.idProduto
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.volume = volume
        self.data_vencimento = date(int(data_vencimento[6:]), int(
            data_vencimento[3:5]), int(data_vencimento[:2]))
        self.data_adicao = date.today()
        self.quantidade = quantidade

    def __str__(self):
        str = ""
        attribs = {"id": self.id,
                   "nome": self.nome,
                   "tipo": self.tipo,
                   "preco": self.preco,
                   "volume": self.volume,
                   "quantidade": self.quantidade,
                   "data_vencimento": self.data_vencimento,
                   "data_adicao": self.data_adicao}

        for key, value in attribs.items():
            if key == "preco":
                str += f" {key}: R$ {value}\n"
            elif key == "data_adicao" or key == "data_vencimento":
                str += f" {key}: {value.strftime('%d/%m/%Y')}\n"
            else:
                str += f" {key}: {value}\n"
        return str

    def getDataVencimento(self):
        return self.data_vencimento.strftime('%d/%m/%Y')
    
    def printProduto(self):
        return f'{self.id} | {self.nome} | R$ {self.preco} | {self.volume}m³ | {self.quantidade} unid. | val. {self.getDataVencimento()}'