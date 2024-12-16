from Models.controleEstoqueModel import ControleEstoque

def main():
    estoque = ControleEstoque()

    while True:
        print('''MENU:
        1 - Adicionar Produto
        2 - Listar Produtos
        3 - Atualizar Produto
        4 - Remover Produto
        5 - Buscar Produto
        0 - Sair
        ''')

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            estoque.adicionar_produto(nome, quantidade, preco)

        elif opcao == 2:
            print("Produtos no estoque:")
            estoque.listar_produtos()

        elif opcao == 3:
            id_produto = (input("Digite o ID ou nome do produto para atualizar: "))
            nova_quantidade = int(input("Digite a nova quantidade (deixe em branco para não alterar): ") or -1)
            novo_preco = float(input("Digite o novo preço (deixe em branco para não alterar): ") or -1)
            if nova_quantidade == -1:
                nova_quantidade = None
            if novo_preco == -1:
                novo_preco = None
            estoque.atualizar_produto(id_produto, nova_quantidade, novo_preco)

        elif opcao == 4:
            id_produto = (input("Digite o ID ou nome do produto para remover: "))
            estoque.remover_produto(id_produto)

        elif opcao == 5:
            busca_opcao = input("Você deseja buscar por (i) ID ou (n) nome? ").lower()
            if busca_opcao == 'i':
                id_produto = int(input("Digite o ID do produto: "))
                estoque.buscar_produto(id_produto=id_produto)
            elif busca_opcao == 'n':
                nome_produto = input("Digite o nome do produto: ")
                estoque.buscar_produto(name=nome_produto)
            else:
                print("Opção inválida!")

        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
