#==========================================
# ARQUIVO: produto.py
# AUTOR: FILIPE MORAES ANGELI
#==========================================
class Produto:
    def __init__(self, id_produto, nome, categoria, preco_unitario, quantidade_estoque):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos.
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        if quantidade > 0:
            self.quantidade_estoque += quantidade
    
    def remover_estoque(self, quantidade):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        if self.esta_disponivel(quantidade):
            self.quantidade_estoque -= quantidade
            return True
        return False

    def atualizar_preco(self, novo_preco):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        if novo_preco > 0:
            self.preco_unitario = novo_preco

    def esta_disponivel(self):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        return self.quantidade_estoque >= quantidade

        # AUTOR: FILIPE MORAES ANGELI