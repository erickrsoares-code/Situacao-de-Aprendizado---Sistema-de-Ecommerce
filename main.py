#==========================================
# ARQUIVO: main.py
# AUTOR: Erick Ricardo Soares
#===================    =======================
import sys
from models.produto import Produto
from models.usuario import Usuario
from models.carrinho import CarrinhoCompras

# Carga inicial de dados
admin = Usuario("1", "admin", "erickadm@techmarket.com", "admin", "Admin")

produtos_bd = {
    "101": Produto("101", "Arroz 5kg", "Alimentos", 28.50, 50),
    "102": Produto("102", "Leite Integral 1L", "Laticínios", 5.20, 100),
    "103": Produto("103", "Detergente", "Limpeza", 2.29, 25)
}

carrinho_atual = CarrinhoCompras()

# Autenticação com Loop
print("--- TechMarket ---")
nome_input = input("Nome de usuário: ").strip()
senha_input = input("Senha: ").strip()

while not admin.autenticar(nome_input, senha_input):
    print("\nCredenciais incorretas! Tente novamente.\n")
    nome_input = input("Nome de usuário: ").strip()
    senha_input = input("Senha: ").strip()

print(f"\nBem-vindo, {admin.nome}! Acesso concedido.")

# Loop do Menu Principal
while True:
    print("\n" + "="*45)
    print("         TECHMARKET - MENU PRINCIPAL")
    print("="*45)
    print("1. Cadastrar Novo Produto & Alterar Estoque")
    print("2. Loja")
    print("0. Sair")
    print("="*45)

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            print("\n--- Cadastro / Gestão de Estoque ---")
            id_produto = input("ID do Produto: ").strip()

            # Caso 1: Atualização de produto existente
            if id_produto in produtos_bd:
                prod = produtos_bd[id_produto]
                print(f"Produto encontrado: {prod.nome} (Estoque atual: {prod.quantidade_estoque})")
                try:
                    nova_qtd = int(input("Digite a nova quantidade total para o estoque: "))
                    prod.quantidade_estoque = nova_qtd
                    print("Estoque atualizado diretamente na memória.")
                except ValueError:
                    print("Quantidade inválida.")
            
            # Caso 2: Instanciação e cadastro de novo produto
            else:
                nome_produto = input("Nome do Produto: ").strip()
                categoria_produto = input("Categoria do Produto: ").strip()
                try:
                    preco_produto = float(input("Preço do Produto (R$): "))
                    quantidade_produto = int(input("Quantidade em Estoque: "))
                    
                    # Criação e salvamento do novo objeto Produto
                    produtos_bd[id_produto] = Produto(
                        id_produto, 
                        nome_produto, 
                        categoria_produto, 
                        preco_produto, 
                        quantidade_produto
                    )
                    print(f"Produto '{nome_produto}' cadastrado com sucesso e disponível na loja!")
                except ValueError:
                    print("Preço ou quantidade inválidos. Operação cancelada.")

        case "2":
            while True:
                print("\n--- Loja TechMarket ---")
                for p in produtos_bd.values():
                    print(f"ID: {p.id_produto} | Nome: {p.nome} | Categoria: {p.categoria} | Preço: R${p.preco_unitario:.2f} | Estoque: {p.quantidade_estoque}")

                print("\nOpções da loja:")
                print("1. Adicionar Produto ao Carrinho")
                print("2. Ver Carrinho")
                print("3. Finalizar Compra")
                print("0. Voltar ao Menu Principal")
                
                opcao_loja = input("Escolha uma opção: ").strip()

                match opcao_loja:
                    case "1":
                        id_p = input("Digite o ID do produto que deseja adicionar: ").strip()
                        if id_p in produtos_bd:
                            try:
                                qtd = int(input("Digite a quantidade desejada: "))
                                # Passando o objeto Produto e a Quantidade como argumentos separados
                                if carrinho_atual.adicionar_item(produtos_bd[id_p], qtd):
                                    print(f"Sucesso! {qtd} unidade(s) de '{produtos_bd[id_p].nome}' adicionada(s) ao carrinho.")
                                else:
                                    print("Estoque insuficiente para a quantidade solicitada.")
                            except ValueError:
                                print("Quantidade inválida.")
                        else:
                            print("Produto não encontrado.")

                    case "2":
                        print("\n--- Carrinho de Compras ---")
                        if not carrinho_atual.itens:
                            print("O carrinho está vazio.")
                        else:
                            for item in carrinho_atual.itens:
                                prod = item["produto"]
                                qtd = item["quantidade"]
                                subtotal = prod.preco_unitario * qtd
                                print(f"Produto: {prod.nome} | Qtd: {qtd} | Preço Un: R${prod.preco_unitario:.2f} | Subtotal: R${subtotal:.2f}")
                            print(f"Total do Carrinho: R${carrinho_atual.calcular_total():.2f}")

                    case "3":
                        if not carrinho_atual.itens:
                            print("Seu carrinho está vazio. Adicione produtos antes de finalizar.")
                        elif carrinho_atual.finalizar_venda():
                            print(f"Compra finalizada com sucesso!")
                            print(f"Total pago: R${carrinho_atual.valor_total:.2f}")
                            carrinho_atual = CarrinhoCompras() # Limpa o carrinho para a próxima venda
                            break  # Sai do loop da loja após finalizar a compra
                        else:
                            print("Erro ao finalizar a compra. Verifique o estoque dos produtos.")

                    case "0":
                        break

                    case _:
                        print("Opção inválida.")
        case "0":
            print("Saindo do sistema. Até logo!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
