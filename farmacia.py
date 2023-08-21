from controller.Farmacia import FarmaciaController
from view.CLI import *


def main():
    controller = FarmaciaController()

    while True:
        menu = '''
        Boas vindas ao nosso sistema:

        1 - Clientes
        2 - Medicamentos
        3 - Vendas
        4 - Emitir Relatório
        0 - Sair
        '''
        print(menu)

        opcao_1 = input('Escolha uma opção: ')
        carrinho = []

        if opcao_1 in ('1', '2', '3', '5'):
            opcao_2 = menu_interno(opcao_1)
            if opcao_2 == '4':
                pass

            # Opção de clientes
            elif opcao_1 == '1':
                if opcao_2 == '1':
                    controller.user_controller.cadastrar_cliente()
                    print("Cliente cadastrado com sucesso!")

                elif opcao_2 == '2':
                    consulta_cpf = ""
                    while len(consulta_cpf) != 11 or not consulta_cpf.isdigit():
                        consulta_cpf = input("Digite o Cpf do cliente que deseja consultar: ")
                        if len(consulta_cpf) != 11 or not consulta_cpf.isdigit():
                            print("CPF inválido!")
                        elif controller.user_controller.check_cpf(consulta_cpf):
                            print("\n::: Cliente localizado! :::")
                        else:
                            print("\n::: Cliente NÃO localizado :::")

                elif opcao_2 == '3':
                    print("\n===== Listagem completa de clientes =====")
                    clientes = controller.user_controller.recuperar_clientes()
                    clientes = sorted(clientes, key=lambda c: c.nome)
                    for cliente in clientes:
                        print(cliente)

            # Opção de Medicamentos
            elif opcao_1 == '2':
                if opcao_2 == '1':
                    controller.drug_controller.cadastrar_medicamento()
                elif opcao_2 == '2':
                    controller.drug_controller.buscar_medicamento()
                elif opcao_2 == '3':
                    drug_top_header()
                    medicamentos = controller.drug_controller.recuperar_medicamentos()
                    print_drug_header()
                    for med in medicamentos:
                        print(med.__str__())
                    print_footer_divider()

        # Opção de Vendas
        elif opcao_1 == '3':
            opcao = '0'
            produtos_venda = []
            cpf_venda = ""
            while len(cpf_venda) != 11 or not cpf_venda.isdigit():
                cpf_venda = input("Digite o Cpf do cliente cadastrado: ")
                if len(cpf_venda) != 11 or not cpf_venda.isdigit():
                    print("CPF inválido!")
                elif not controller.user_controller.check_cpf(cpf_venda):
                    print("\n::: Cliente NÃO localizado :::")
                else:
                    cliente = controller.user_controller.recuperar_clientes(cpf=cpf_venda)
                    while opcao == '0':
                        medicamentos = controller.drug_controller.recuperar_medicamentos()
                        print_drug_header()
                        for medicamento in medicamentos:
                            print(medicamento.__str__())

                        id_medicamento = input('Escolha o ID do medicamento que deseja incluir no carrinho: ')
                        medicamento = controller.drug_controller.recuperar_medicamentos(identificador=id_medicamento)

                        flag_continua_compra = True
                        if medicamento.receita_necessaria is True:
                            verificar_receita = input(
                                f"ATENÇÃO! O medicamento '{medicamento.nome}' é de uso controlado. "
                                f"Você possui a receita? (S/N): "
                            )
                            if verificar_receita.upper() == "N":
                                print("É necessario a receita do medicamento solicitado.")
                                flag_continua_compra = False

                        if flag_continua_compra is True:
                            qtd_medicamento = int(input('Digite a quantidade desejada: '))
                            for _ in range(qtd_medicamento):
                                produtos_venda.append(medicamento)

                        opcao = input('Deseja adicionar outro medicamento: 1 - Sim ou 2 - Não: ')
                        if opcao == '1':
                            opcao = '0'
                        else:
                            controller.sell_controller.registar_venda(produtos=produtos_venda, cliente=cliente)

        elif opcao_1 == '4':
            for vendas in carrinho:
                print('Dentro do vendas 5')
                print(vendas)

        elif opcao_1 == '0':
            controller.sell_controller.emitir_relatorio_de_vendas()
            print("Execução finalizada!")
            break
        else:
            print('A opção escolhida é inválida!! ')


if __name__ == '__main__':
    main()
