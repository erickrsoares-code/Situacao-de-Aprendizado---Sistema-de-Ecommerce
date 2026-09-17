# ========================================================
# ARQUIVO: models/produto.py
# AUTOR: Filipe Moraes Angeli
# ========================================================

class Produto:
    # AUTOR: Filipe Moraes Angeli
    def __init__(self, id_produto, nome, categoria, preco_unitario, quantidade_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = float(preco_unitario)
        self.quantidade_estoque = int(quantidade_estoque)

    # AUTOR: Filipe Moraes Angeli
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade_estoque += quantidade
            return True
        return False

    # AUTOR: Filipe Moraes Angeli
    def remover_estoque(self, quantidade):
        if self.esta_disponivel(quantidade):
            self.quantidade_estoque -= quantidade
            return True
        return False

    # AUTOR: Filipe Moraes Angeli
    def atualizar_preco(self, novo_preco):
        if novo_preco > 0:
            self.preco_unitario = float(novo_preco)
            return True
        return False

    # AUTOR: Filipe Moraes Angeli
    def esta_disponivel(self, quantidade=1):
        return self.quantidade_estoque >= quantidade