from menu import (
    exibir_menu,
    menu_cliente,
    menu_servico,
    menu_ordem_servico
)

def main():
    while True:
        exibir_menu()
        try:
            indice = int(input(">>> "))
        except ValueError:
            print("Opção Inválida. Digite um numero.")
            continue

        match indice:
            case 1:
                menu_cliente()

            case 2:
                menu_servico()

            case 3:
                menu_ordem_servico()

            case 0:
                print("Encerrando AutoCare...")
                break

            case _:
                print("Opção Inválida! Tente novamente.")

if __name__=="__main__":
    main()