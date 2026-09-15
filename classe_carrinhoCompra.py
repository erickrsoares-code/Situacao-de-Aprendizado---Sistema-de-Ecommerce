class CarrinhoCompra:
    def __init__(self, valor_total=0, status_compra="aberto"):
        self.valor_total = valor_total
        self.status_compra = status_compra
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)

    def calcular_total(self):  
        total = sum(item.preco for item in self.itens)
        return total

    def finalizar_venda(self):
        if self.status_compra == "aberto":
            self.status_compra = "finalizado"
            self.valor_total = self.calcular_total()
        else:
            print("A compra já foi finalizada.")
        