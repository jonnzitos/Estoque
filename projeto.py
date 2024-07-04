estoque = {}

def adicionar(nome, quantidade):
    if nome in estoque:
        print(f"Produto {nome} já existe no estoque. Use a opção de atualizar quantidade.")
    else:
        estoque[nome] = quantidade
        print(f"Produto {nome} adicionado com quantidade {quantidade}.")

def atualizar(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do produto {nome} atualizada para {quantidade}.")
    else:
        print(f"Produto {nome} não encontrado no estoque. Use a opção de adicionar novo produto.")

def remover(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Produto {nome} removido do estoque.")
    else:
        print(f"Produto {nome} não encontrado no estoque.")

def visualizar():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("Estoque atual:")
        for nome, quantidade in estoque.items():
            print(f"{nome}: {quantidade}")

def menu():
    while True:
        print("\n1. Adicionar novo produto")
        print("2. Atualizar quantidade de produto")
        print("3. Remover produto")
        print("4. Visualizar estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            adicionar(nome, quantidade)
        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Nova quantidade: "))
            atualizar(nome, quantidade)
        elif opcao == '3':
            nome = input("Nome do produto: ")
            remover(nome)
        elif opcao == '4':
            visualizar()
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
