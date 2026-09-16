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
    print("\n" + "="*45)
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
            
