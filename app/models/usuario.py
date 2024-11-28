from sys import excepthook
from .. import mysql

import bcrypt
import re


class Usuario:
    def __init__(self, nome_usuario, email, senha, data_registro, roteiros, viagens, favoritos):
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha
        self.data_registro = data_registro
        self.roteiros = roteiros
        self.viagens = viagens
        self.favoritos = favoritos


    def salvar_usuario(self):
        cursor = mysql.connection.cursor()

        validacao = self.validar_dados(self.nome_usuario, self.email, self.senha)
        if validacao:
            print(validacao)
            return None

        try:
            cursor.execute("SELECT * FROM usuario WHERE Email = %s", (self.email))
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                print("Usuário já existente com este email")
                return None

            senha_hashed = self.hash_senha(self.senha)

            cursor.execute("""
                            INSERT INTO Usuario (Nome_Usuario, Email, Senha, Data_Registro, Roteiros, Viagens, Favoritos)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """, (
            self.nome_usuario, self.email, self.senha, self.data_registro, self.roteiros, self.viagens, self.favoritos))

            mysql.connection.commit()

            novo_id = cursor.lastrowid
            return novo_id

        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            return None

        finally:
            cursor.close()


    @staticmethod
    def obter_usuario_por_id(id_usuario):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("SELECT * FROM usuario WHERE ID = %s", (id_usuario))
            usuario = cursor.fetchone()
            return usuario

        except Exception as e:
            print(e)
            return None

        finally:
            cursor.close()


    @staticmethod
    def obter_usuario_por_email(email):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("SELECT * FROM usuario WHERE Email = %s", (email))
            usuario = cursor.fetchone()
            return usuario

        except Exception as e:
            print(e)
            return None

        finally:
            cursor.close()


    @staticmethod
    def atualizar_usuario(self, id_usuario):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("""
                            UPDATE Usuario
                            SET Nome_Usuario = %s, Email = %s, Senha = %s, Data_Registro = %s, Roteiros = %s, Viagens = %s, Favoritos = %s
                            WHERE ID = %s
                        """, (
            self.nome_usuario, self.email, self.senha, self.data_registro, self.roteiros, self.viagens, self.favoritos,
            id_usuario))
            mysql.connection.commit()
            return cursor.rowcount > 0

        except Exception as e:
            print(e)
            return None

        finally:
            cursor.close()


    @staticmethod
    def deletar_usuario(id_usuario):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("DELETE FROM usuario WHERE ID = %s", (id_usuario))
            mysql.connection.commit()
            return cursor.rowcount > 0

        except Exception as e:
            print(e)
            return False

        finally:
            cursor.close()


    @staticmethod
    def hash_senha(senha):
        return bcrypt.hashpw(senha, bcrypt.gensalt()).decode('utf-8')


    @staticmethod
    def verificar_senha(senha, hash_senha):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))


    @staticmethod
    def validar_dados(nome_usuario, senha):
        if len(nome_usuario) < 5:
            return "O nome de usuário deve ter pelo menos 5 caracteres"

        if len(senha) < 8:
            return "A senha deve ter mais de 8 caracteres"

        return None


    @staticmethod
    def autenticar_usuario(email, senha):
        cursor = mysql.connection.cursor()

        try:
            cursor.execute("SELECT * FROM usuario WHERE Email = %s", (email))
            usuario = cursor.fetchone()

            if usuario and Usuario.verificar_senha(senha, usuario['senha']):
                return usuario['id_usuario']
            else:
                print("Email ou senha incorretos")
                return None

        except Exception as e:
            print(f"Erro na autenticação: {e}")
            return None

        finally:
            cursor.close()