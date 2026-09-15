#==========================================
# ARQUIVO: carrinho.py
# AUTOR: Jorje Henrique Mazera Soares
#==========================================
class CarrinhoCompra:
    def __init__(self, valor_total=0, status_compra="aberto"):
        # Programado por: Jorje Henrique Mazera Soares
        # Funcao base cria um carrinho de compras.
        self.valor_total = valor_total
        self.status_compra = status_compra
        self.itens = []

    def adicionar_item(self, item):
        # Programado por: Jorje Henrique Mazera Soares
        # Funcao que adiciona itens ao carrinho.
        self.itens.append(item)

    def remover_item(self, item):
        # Programado por: Jorje Henrique Mazera Soares
        # Funcao que remove itens do carrinho.
        if item in self.itens:
            self.itens.remove(item)

    def calcular_total(self):  
        # Programado por: Jorje Henrique Mazera Soares
        # Funcao que calcula o total do carrinho.
        total = sum(item.preco for item in self.itens)
        return total

    def finalizar_venda(self):
        # Programado por: Jorje Henrique Mazera Soares
        # Funcao que finaliza a compra.
        if self.status_compra == "aberto":
            self.status_compra = "finalizado"
            self.valor_total = self.calcular_total()
        else:
            print("A compra já foi finalizada.")
        