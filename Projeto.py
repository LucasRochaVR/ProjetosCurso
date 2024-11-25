import sqlite3  

def criar_tabela(cursor):
    
    sql='''
        CREATE TABLE IF NOT EXISTS produtos(
        ID  INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        quantidade INTEGER,
        preco INTEGER
        )                   
    '''
        
    cursor.execute(sql)
    
     
    
def main():
    conn = sqlite3.connect('C:/Users/Aluno/Desktop/LUCAS ROCHA/projeto.db')
    
    cursor = conn.cursor()
    
    criar_tabela(cursor)
    conn.commit()
    
    # menu
    while True:
        print('''MENU:
        1-ADICIONAR PRODUTO
        2-LISTAR PRODUTOS
        3-ATUALIZAR PRODUTO
        4-REMOVER PRODUTO
        5-BUSCAR PRODUTO 
        6-VALOR TOTAL DO ESTOQUE
        0-SAIR      
        ''')
        opicao = int(input("ESCOLHA UMA OPÇÃO:"))
        
    
        if opicao == 1:
            name = input("nome do produto:")
            quantidade = int(input("quantidade em estoque:"))
            preco = float(input("qual preço do produto:"))
            
            if quantidade < 0:  
                print("Valores inseridos não pode ser negativo.") 
                continue
            
            if preco < 0:
                print("Valores inseridos não pode ser negativo.") 
                continue   
        
            cursor.execute(f'INSERT INTO produtos(name,quantidade,preco) VALUES ("{name}","{quantidade}","{preco}")')
            conn.commit()
            
        
        if opicao == 2:
            
            cursor.execute('SELECT * FROM produtos')
            print(cursor.fetchall())
            
                
        if opicao == 3:
            name = input("nome:")
            quantidade = int(input("quantidade em estoque:"))
            preco = float(input("qual preço do produto:"))
            cursor.execute(f'UPDATE produtos set name = "{name}",quantidade = "{quantidade}",preco = "{preco}" WHERE name = "{name}"') 
            conn.commit()
            
        if opicao == 4:
            name = input("nome ou id:")
            cursor.execute(f'DELETE FROM produtos WHERE name ="{name}" OR id = "{name}"') 
            conn.commit()
            
        if opicao == 5:
            
            id = input("selecione name ou id:")
            cursor.execute(F'SELECT * FROM produtos WHERE ID = "{id}" OR name = "{id}"') 
            print(cursor.fetchall())
         
        if opicao == 6:
            
            cursor.execute('SELECT SUM(quantidade * preco) AS total_venda FROM produtos') 
            print(cursor.fetchall())
            
        if opicao == 0:
        
            break
    conn.close()
    
if __name__== "__main__":
        main()
        