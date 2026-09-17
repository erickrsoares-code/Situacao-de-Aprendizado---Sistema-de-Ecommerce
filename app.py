from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.produto import Produto
from models.carrinho import CarrinhoCompras

app = Flask(__name__)
app.secret_key = 'techmark_supermercado_chave_secreta_segura'

# Base de Produtos original mantida
PRODUTOS = [
    Produto(1, "Picanha Bovina Grill Premium", "carnes", 69.90, 15),
    Produto(2, "Contra Filé Bovino Fatiado", "carnes", 45.90, 20),
    Produto(3, "Coxa e Sobrecoxa de Frango", "carnes", 16.90, 30),
    Produto(4, "Costela Bovina do Dianteiro", "carnes", 32.90, 10),
    Produto(5, "Linguiça Toscana para Churrasco", "carnes", 21.90, 25),
    Produto(6, "Maçã Gala Selecionada Orgânica", "hortifruti", 8.99, 50),
    Produto(7, "Suco de Laranja Integral", "hortifruti", 12.90, 40),
    Produto(8, "Banana Prata Climatizada", "hortifruti", 6.49, 60),
    Produto(9, "Tomate Italiano Selecionado", "hortifruti", 7.89, 45),
    Produto(10, "Refrigerante Cola Zero Açúcar", "bebidas", 4.50, 100),
    Produto(11, "Cerveja Heineken Premium", "bebidas", 6.99, 80),
    Produto(12, "Água Mineral Sem Gás", "bebidas", 2.20, 120),
    Produto(13, "Pão Francês Artesanal", "padaria", 6.50, 40),
    Produto(14, "Croissant Folhado de Queijo", "padaria", 8.90, 20),
    Produto(15, "Queijo Mussarela Fatiado", "frios", 14.90, 35),
    Produto(16, "Peito de Peru Defumado", "frios", 12.50, 30)
]

# Imagens mapeadas para manter a estética
IMAGENS = {
    1: "https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=400",
    2: "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
    3: "https://images.unsplash.com/photo-1587593810167-a84920ea0781?w=400",
    4: "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=400",
    5: "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=400",
    6: "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400",
    7: "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400",
    8: "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400",
    9: "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=400",
    10: "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    11: "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=400",
    12: "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=400",
    13: "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400",
    14: "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=400",
    15: "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=400",
    16: "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=400" 
}

CARRINHO = CarrinhoCompras()


# 3.2 TELA DE LOGIN (index.html)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        if usuario == 'admin' and senha == 'admin':
            session['usuario'] = usuario
            return redirect(url_for('menu'))
        else:
            flash("Usuário ou senha incorretos! Tente admin/admin")

    return render_template('index.html')


# 3.3 MENU PRINCIPAL (menu.html)
@app.route('/menu')
def menu():
    if 'usuario' not in session: return redirect(url_for('login'))
    return render_template('menu.html')


# 3.4 ESTOQUE E CADASTRO (cadastro-prod.html)
@app.route('/cadastro-prod', methods=['GET', 'POST'])
def cadastro_prod():
    if 'usuario' not in session: return redirect(url_for('login'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        preco = float(request.form.get('preco', 0))
        estoque = int(request.form.get('estoque', 0))

        novo_id = len(PRODUTOS) + 1
        PRODUTOS.append(Produto(novo_id, nome, categoria, preco, estoque))
        # Imagem genérica para novos
        IMAGENS[novo_id] = "https://images.unsplash.com/photo-1542838132-92c53300491e?w=400"
        flash(f"Produto {nome} cadastrado com sucesso!")
        return redirect(url_for('cadastro_prod'))

    return render_template('cadastro-prod.html', produtos=PRODUTOS)

@app.route('/atualizar-estoque', methods=['POST'])
def atualizar_estoque():
    for prod in PRODUTOS:
        nova_qtd = request.form.get(f'qtd_{prod.id}')
        if nova_qtd: prod.quantidade_estoque = int(nova_qtd)
    flash("Estoque atualizado!")
    return redirect(url_for('cadastro_prod'))


# 3.5 VITRINE / PDV (loja.html)
@app.route('/loja')
def loja():
    if 'usuario' not in session: return redirect(url_for('login'))
    return render_template('loja.html', produtos=PRODUTOS, imagens=IMAGENS)

@app.route('/adicionar-carrinho/<int:prod_id>', methods=['POST'])
def adicionar_carrinho(prod_id):
    prod = next((p for p in PRODUTOS if p.id_produto == prod_id), None)
    if prod and prod.quantidade_estoque > 0:
        CARRINHO.adicionar_item(prod, 1)
        flash(f"{prod.nome} adicionado ao carrinho!")
    else:
        flash("Produto sem estoque!")
    return redirect(url_for('loja'))


# 3.6 CARRINHO (carrinho.html)
@app.route('/carrinho')
def carrinho():
    if 'usuario' not in session: return redirect(url_for('login'))
    total = sum(item["produto"].preco_unitario * item["quantidade"] for item in CARRINHO.itens)
    return render_template('carrinho.html', carrinho=CARRINHO, total=total, imagens=IMAGENS)

@app.route('/remover-carrinho/<int:prod_id>', methods=['POST'])
@app.route('/remover-carrinho/<int:prod_id>', methods=['POST'])
def remover_carrinho(prod_id):
    id_remover = int(prod_id)
    
    # Mantém no carrinho apenas os itens cujo ID seja diferente do que estamos removendo
    CARRINHO.itens = [item for item in CARRINHO.itens if item["produto"].id_produto != id_remover]
    
    return redirect(url_for('carrinho'))

@app.route('/finalizar-compra', methods=['POST'])
def finalizar_compra():
    if CARRINHO.finalizar_venda():
        CARRINHO.itens.clear() # Limpa após finalizar
        flash("Venda finalizada! Estoque baixado com sucesso.")
    else:
        flash("Erro ao finalizar venda (Estoque insuficiente).")
    return redirect(url_for('loja'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)