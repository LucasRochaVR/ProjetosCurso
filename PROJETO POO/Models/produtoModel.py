class Produto:
    def __init__(self, id, name, quantidade, preco):
        self.id = id
        self.name = name
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f'ID: {self.id}, Nome: {self.name}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}'
