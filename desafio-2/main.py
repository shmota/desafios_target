from estoque_controller import Estoque

if __name__ == "__main__":

    estoque = Estoque("desafio-2/estoque.json")

    while True:
        print("MENU".center(30, "="))
        print("1 - Entrada de Produto")
        print("2 - Saida de Produto")
        print("3 - Sair")

        opcao = int(input("Digite sua opcao: "))

        if opcao == 1:
            estoque.registrar_entrada()
            continue
        
        elif opcao == 2:
            estoque.registrar_saida()
            continue

        elif opcao == 3:
            break
        
        else:
            print("Opcao invalida!")