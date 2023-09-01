def mostrar_lista(lista):
    print("Lista de Compras")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

def colocar_itens(lista, item):
    lista.append(item)
    print(f"{item} foi colocado na lista.")

def editar_itens(lista, indice, novo_produto):
    if 0 <= indice < len(lista):
        lista[indice] = novo_produto
        print("Mudança feita com sucesso")
    else:
        print("Produto sem alteração")

def remover_produto(lista, indice):
    if 0 <= indice < len(lista):
        produto_removido = lista.pop(indice)
        print(f"{produto_removido} foi removido da lista")
    else:
        print("(OPÇÃO INVÁLIDA) A alteração não foi realizada")

def main():
    lista_de_compra = []

    while True:
        print("Escolha uma das Opções:")
        print("(1) Mostrar lista")
        print("(2) Adicionar Produtos")
        print("(3) Editar os produtos")
        print("(4) Remover um produto")
        print("(5) Sair")

        opcao = input()

        if opcao == "1":
            mostrar_lista(lista_de_compra)
        elif opcao == "2":
            item = input("Digite o produto que vai ser colocado na lista: ")
            colocar_itens(lista_de_compra, item)
        elif opcao == "3":
            indice = int(input("Digite o número do produto que vai ser editado: ")) - 1
            novo_produto = input("Coloque o novo produto: ")
            editar_itens(lista_de_compra, indice, novo_produto)
        elif opcao == "4":
            mostrar_lista(lista_de_compra)
            indice = int(input("Digite o número do produto que vai ser removido: ")) - 1
            remover_produto(lista_de_compra, indice)
        elif opcao == "5":
            print("Saindo")
            break
        else:
            print("(OPÇÃO INVÁLIDA) Escolha um número válido")

if __name__ == "__main__":
    main()
