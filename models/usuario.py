# ========================================================
# ARQUIVO: models/usuario.py
# AUTOR: Charles Battisti
# ========================================================

class Usuario:
    # AUTOR: Charles Battisti
    def __init__(self, id_usuario, nome, email, senha, tipo_permissao):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo_permissao = tipo_permissao

    # AUTOR: Charles Battisti
    def autenticar(self, nome, senha):
        login_valido = (self.nome == nome or self.email == nome)
        return login_valido and self.senha == senha

    # AUTOR: Charles Battisti
    def alterar_senha(self, nova_senha):
        if len(nova_senha) >= 4:
            self.senha = nova_senha
            return True
        return False

    # AUTOR: Charles Battisti
    def obter_dados_perfil(self):
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "tipo_permissao": self.tipo_permissao
        }