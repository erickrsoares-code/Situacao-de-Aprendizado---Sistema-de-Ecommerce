# ========================================================
# ARQUIVO: models/carrinho.py
# AUTOR: Jorge Henrique Mazera Soares
# ========================================================

class CarrinhoCompras:
    # AUTOR: Jorge Henrique Mazera Soares
    def __init__(self, valor_total=0.0, status_compra="Aberto"):
        self.valor_total = valor_total
        self.status_compra = status_compra
        self.itens = []

    # AUTOR: Jorge Henrique Mazera Soares
    def adicionar_item(self, produto, quantidade):
        if produto.esta_disponivel(quantidade):
            self.itens.append({"produto": produto, "quantidade": quantidade})
            self.calcular_total()
            return True
        return False

    # AUTOR: Jorge Henrique Mazera Soares
    def remover_item(self, produto):
        self.itens = [i for i in self.itens if i["produto"] != produto]
        self.calcular_total()

    # AUTOR: Jorge Henrique Mazera Soares
    def calcular_total(self):
        self.valor_total = sum(item["produto"].preco_unitario * item["quantidade"] for item in self.itens)
        return self.valor_total

    # AUTOR: Jorge Henrique Mazera Soares
    def finalizar_venda(self):
        if not self.itens or self.status_compra != "Aberto":
            return False

        for item in self.itens:
            prod = item["produto"]
            qtd = item["quantidade"]
            if not prod.remover_estoque(qtd):
                print(f"Erro: Estoque insuficiente para {prod.nome}.")
                return False

        self.status_compra = "Finalizado"
        return True