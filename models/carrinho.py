#==========================================
# ARQUIVO: carrinho.py
# AUTOR: Jorge Henrique Mazera Soares
#===================    =======================
class CarrinhoCompras:
    def __init__(self, valor_total=0, status_compra="aberto"):
        # Programado por: Jorge Henrique Mazera Soares
        # Funcao base cria um carrinho de compras.
        self.valor_total = valor_total
        self.status_compra = status_compra
        self.itens = []

    def adicionar_item(self, item):
        # Programado por: Jorge Henrique Mazera Soares
        # Funcao que adiciona itens ao carrinho.
        if produto.esta_disponivel(quantidade):
            self.itens.append({"produto": produto, "quantidade": quantidade})
            self.calcular_total()
            return True
        return False

    def remover_item(self, item):
        # Programado por: Jorge Henrique Mazera Soares
        # Funcao que remove itens do carrinho.
        if item in self.itens:
            self.itens.remove(item)

    def calcular_total(self):  
        # Programado por: Jorge Henrique Mazera Soares
        # Funcao que calcula o total do carrinho.
        total = sum(item.preco_unitario for item in self.itens)
        return total

    def finalizar_venda(self):
        # Programado por: Jorge Henrique Mazera Soares
        # Funcao que finaliza a compra.
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
# AUTOR: Jorge Henrique Mazera Soares