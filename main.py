from models.produto import Produto
from models.usuario import Usuario
from models.carrinho import CarrinhoCompras

admin = Usuario("1", "admin", "erickadm@techmarket.com", "admin", "Admin")

produtos_bd = {
        "101": Produto("101", "Arroz 5kg", "Alimentos", 28.50, 50),
        "102": Produto("102", "Leite Integral 1L", "Laticínios", 5.20, 100),
        "103": Produto("103", "Detergente", "Limpeza", 2.29, 25)
}

carrinho_atual = CarrinhoCompras()

print("--- TechMarket ---")
nome_input = input("Nome de usuário: ").strip()
senha_input = input("Senha: ").strip()

if not admin.autenticar(nome_input, senha_input):
    print("\nCredenciais incorretas!")
    

print(f"\n Bem-vindo, {admin.nome}! Acesso concedido.")

while True:
    print("\n", "="*45)
    print("         TECHMARKET - MENU PRINCIPAL")
    print("="*45)
    print("1. Cadastrar Novo Produto & Alterar Estoque")
    print("2. Loja")
    print("0. Sair")
    print("="*45)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\n--- Cadastro de Produto ---")
            id_produto = input("ID do Produto: ").strip()
            if id_produto in produtos_db:
                print(f"Produto encontrado: {produtos_db[id_produto].nome} (Estoque atual: {produtos_db[id_produto].quantidade_estoque})")
                try:
                    nova_qtd = int(input("Digite a nova quantidade total para o estoque: "))
                    produtos_db[id_produto].quantidade_estoque = nova_qtd
                    print(" Estoque atualizado diretamente na memória.")
                except ValueError:
                    print("Quantidade inválida.")
                continue
            nome_produto = input("Nome do Produto: ")
            categoria_produto = input("Categoria do Produto: ")
            try:
                preco_produto = float(input("Preço do Produto: "))
                quantidade_produto = int(input("Quantidade em Estoque: "))
            except ValueError:
                print("Preço ou quantidade inválidos. Tente novamente.")
                continue

        case "2":
            print("\n--- Loja ---")
            for p in produtos_bd.values():
                print(f"ID: {p.id_produto} | Nome: {p.nome} | Categoria: {p.categoria} | Preço: R${p.preco_unitario:.2f} | Estoque: {p.quantidade_estoque}")

            print("\n Opções da loja:")
            print("1. Adicionar Produto ao Carrinho")
            print("2. Ver Carrinho")
            print("3. Finalizar Compra")
            print("0. Voltar ao Menu Principal")
            try:
                opcao_loja = input("Escolha uma opção: ")
            except ValueError:
                print("Opção inválida. Tente novamente.")
                continue
            match opcao_loja:
                case "1":
                    id_produto = input("Digite o ID do produto que deseja adicionar ao carrinho: ").strip()
                    if id_produto in produtos_bd:
                        try:
                            quantidade = int(input("Digite a quantidade desejada: "))
                            if produtos_bd[id_produto].esta_disponivel(quantidade):
                                carrinho_atual.adicionar_item({"produto": produtos_bd[id_produto], "quantidade": quantidade})
                                print(f"{quantidade} unidade(s) de {produtos_bd[id_produto].nome} adicionada(s) ao carrinho.")
                            else:
                                print("Quantidade solicitada não disponível em estoque.")
                        except ValueError:
                            print("Quantidade inválida. Tente novamente.")
                    else:
                        print("Produto não encontrado.")
                case "2":
                    print("\n--- Carrinho de Compras ---")
                    if not carrinho_atual.itens:
                        print("Carrinho vazio.")
                    else:
                        for item in carrinho_atual.itens:
                            prod = item["produto"]
                            qtd = item["quantidade"]
                            print(f"Produto: {prod.nome} | Quantidade: {qtd} | Preço Unitário: R${prod.preco_unitario:.2f} | Subtotal: R${prod.preco_unitario * qtd:.2f}")
                        print(f"Total do Carrinho: R${carrinho_atual.calcular_total():.2f}")
                case "3":
                    if carrinho_atual.finalizar_venda():
                        print("Compra finalizada com sucesso!")
                        print(f"Total pago: R${carrinho_atual.valor_total:.2f}")
                        carrinho_atual = CarrinhoCompras() 
                    else:
                        print("Erro ao finalizar a compra. Verifique o estoque dos produtos.")
                case "0":
                    continue
                case _:
                    print("Opção inválida. Tente novamente.")