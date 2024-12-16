import sqlite3
from Models.produtoModel import Produto

class ControleEstoque:
    def __init__(self):
        # Conectar ao banco de dados
        self.conn = sqlite3.connect('estoque.db') 
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.conn.commit()

    def criar_tabela(self):
        # Criar a tabela de produtos, se não existir
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantidade INTEGER,
            preco REAL
        )
        ''')
        self.conn.commit()

    def adicionar_produto(self, name, quantidade, preco):
        # Adicionar um produto no banco
        self.cursor.execute('''
        INSERT INTO produtos (name, quantidade, preco) 
        VALUES (?, ?, ?)
        ''', (name, quantidade, preco))
        self.conn.commit()
        print(f'Produto {name} adicionado com sucesso.')

    # Lista os produtos do banco de dados e cria objetos Produto com os dados retornados
    def listar_produtos(self):
        self.cursor.execute('SELECT * FROM produtos')
        produtos = self.cursor.fetchall()
        for produto in produtos:
            print(produto) 
            print(Produto(produto[0], produto[1], produto[2], produto[3]))

    def atualizar_produto(self, nome=None, id=None, quantidade=None, preco=None):
        if nome is None and id is None:
            print("Você deve fornecer o nome ou o ID do produto para atualizar.")
            return

        # Verifica se foi fornecido nome ou id para localizar o produto
        if nome:
            self.cursor.execute('SELECT * FROM produtos WHERE name = ?', (nome,))
        elif id:
            self.cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))

        produto = self.cursor.fetchone()
        
        if produto is None:
            print("Produto não encontrado.")
            return
        
        # Se o nome, quantidade ou preço forem fornecidos, atualiza o valor
        if quantidade is not None:
            self.cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (quantidade, produto[0]))

        if preco is not None:
            self.cursor.execute('UPDATE produtos SET preco = ? WHERE id = ?', (preco, produto[0]))

        self.conn.commit()
        print(f'O produto foi atualizado com sucesso.')


    def remover_produto(self, nome=None, id=None):
        if nome is None and id is None:
            print("Você deve fornecer o nome ou o ID do produto para remover.")
            return

        # Verifica se foi fornecido nome ou id para localizar o produto
        if nome:
            self.cursor.execute('SELECT * FROM produtos WHERE name = ?', (nome,))
        elif id:
            self.cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))

        produto = self.cursor.fetchone()

        if produto is None:
            print("Produto não encontrado.")
            return

        # Deleta o produto encontrado pelo nome ou id
        if nome:
            self.cursor.execute('DELETE FROM produtos WHERE name = ?', (nome,))
        elif id:
            self.cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))

        self.conn.commit()
        
        if self.cursor.rowcount > 0:
            print(f'O produto foi removido com sucesso.')
        else:
            print("Erro ao remover o produto.")


    def buscar_produto(self, id_produto=None, name=None):
        # Buscar produto pelo nome ou ID
        if id_produto:
            self.cursor.execute('SELECT * FROM produtos WHERE id = ?', (id_produto,))
        elif name:
            self.cursor.execute('SELECT * FROM produtos WHERE name = ?', (name,))
        else:
            print("Por favor, forneça um nome ou ID para a busca.")
            return

        produtos = self.cursor.fetchall()
        if produtos:
            for produto in produtos:
                print(Produto(produto[0], produto[1], produto[2], produto[3]))
        else:
            print("Produto não encontrado.")

    def __del__(self):
        # Fechar a conexão com o banco ao finalizar
        self.conn.close()
