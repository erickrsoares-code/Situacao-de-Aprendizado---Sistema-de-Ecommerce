#==========================================
# ARQUIVO: produto.py
# AUTOR: FILIPE MORAES ANGELI
#==========================================
class produto:
    def __init__(self, id_produto, nome, categoria, preco_unitario, quantidade_estoque):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos.
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque

    def adiciona_estoque(self, quantidade):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        self.quantidade_estoque += quantidade
    
    def remove_estoque(self, quantidade):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
        else:
            print("Nao temos esse produto em estoque.")

    def atualizar_preco(self, novo_preco):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        self.preco_unitario = novo_preco

    def esta_disponivel(self):
        # Programado por: Felipe Morais Angeli
        # Funcao base da class adciona novos produtos. 
        return self.quantidade_estoque > 0
    