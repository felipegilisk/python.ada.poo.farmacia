import os


def clear_cli():
    os.system("clear" if os.name != "nt" else "cls")


def print_drug_header() -> None:
    print("|   ID   |              Nome              | Receita Obrigatória | Valor Unitário |   Tipo   |")


def print_footer_divider() -> None:
    print("|-------------------------------------------------------------------------------------------|")


def drug_top_header() -> None:
    print(
        "|-------------------------------------------------------------------------------------------|"
    )
    print(
        "|                                   Lista de Medicamentos                                   |"
    )
    print(
        "|-------------------------------------------------------------------------------------------|"
    )


def main_app_header() -> None:
    print(
        "|-------------------------------------------------------------------------------------------|"
    )
    print(
        "|                                        SIGFarm-ADA                                        |"
    )
    print(
        "|-------------------------------------------------------------------------------------------|"
    )


def menu_interno(opcao: str):
    """
    Segundo menu de navegação
    """

    switch_opcao = {
        '1': 'Clientes',                        1: 'Clientes',
        '2': 'Medicamentos',                    2: 'Medicamentos',
        '3': 'Vendas',                          3: 'Vendas',
        '4': 'Emitir Relatório',                4: 'Emitir Relatório'
    }

    menu_atual = f""" ::: Menu {switch_opcao.get(opcao)} :::
    1 - Cadastrar
    2 - Consultar
    3 - Listagem completa
    4 - Voltar
    """

    opcao_selecionada = '0'
    while opcao_selecionada not in ('1', '2', '3', '4'):
        clear_cli()
        main_app_header()
        print(menu_atual)
        print_footer_divider()

        opcao_selecionada = input("Escolha uma opção: ")

        if opcao_selecionada not in ('1', '2', '3', '4'):
            print("Opção inválida!")

    return opcao_selecionada
