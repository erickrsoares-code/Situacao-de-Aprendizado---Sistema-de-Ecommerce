#==========================================
# ARQUIVO: usuario.py
# AUTOR: Charles Battisti
#==========================================

class Usuario:
    def __init__(self, id_usuario, nome, email, senha, tipo_permissao):
        # Programado por: Charles Battisti
        # Funcao base da class adciona novos usuarios.
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo_permissao = tipo_permissao

    def autenticar(self, nome, senha):
        # Programado por: Charles Battisti
        # Funcao Autentica o usuário com base no email e senha fornecidos.
        login_valido = (self.nome == nome or self.email == nome)
        return login_valido and self.senha == senha

    def alterar_senha(self, nova_senha):
        # Programado por: Charles Battisti
        # Funcao que altera a senha do usuário.
        if len(nova_senha) >= 4:
            self.senha = nova_senha

    def obter_dados_perfil(self):
        # Programado por: Charles Battisti
        # Funcao que retorna os dados do perfil do usuário.
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "email": self.email,
            "tipo_permissao": self.tipo_permissao
        }
# AUTOR: Charles Battisti