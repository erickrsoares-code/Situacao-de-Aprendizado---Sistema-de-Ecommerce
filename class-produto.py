#================================================
#AUTOR:FILIPE MORAES ANGELI
#ARQUIVO:CLASS PRODUTO.PY
#CODIGO FEITO COMPLETAMENTE POR FILIPE MORAES ANGELI
#================================================

class produto:
    def __init__(self, id_produto, nome, categoria, preco_unitario, quantidade_estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.quantidade_estoque = quantidade_estoque

    def adiciona_estoque(self, quantidade): 
        self.quantidade_estoque += quantidade
    
    def remove_estoque(self, quantidade):
        if quantidade <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade
        else:
            print("Nao temos esse produto em estoque.")

    def atualizar_preco(self, novo_preco):
        self.preco_unitario = novo_preco

    def esta_disponivel(self):
        return self.quantidade_estoque > 0
    