from datetime import date, datetime
from models.cliente import Cliente
from models.medicamento import MedicamentoFitoterapico, MedicamentoQuimioterapico, MedicamentoVendido
from models.laboratorio import Laboratorio
from models.venda import Venda
from functions.menus import menu_interno, menu_vendas
from functions.cadastros import cadastra_cliente, cadastra_medicamento, grava_registro, cadastros_iniciais
from functions.relatorio import emitir_relatorio_de_vendas, localizar, carrega_registros
from functions.util import cpf_ja_cadastrado, calcular_desconto


def main():
    cadastros_iniciais()

    while True:
        menu = '''
        Boas vindas ao nosso sistema:

        1 - Clientes
        2 - Medicamentos Quimioterápicos
        3 - Medicamentos Fitoterápicos
        4 - Vendas
        5 - Emitir Relatório
        6 - Sair
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
                clientes = carrega_registros('clientes')
                if opcao_2 == '1':
                    novo_cliente = cadastra_cliente()
                    
                    if cpf_ja_cadastrado(novo_cliente.cpf):
                        print(f"Já existe um cliente cadastrado com o cpf {novo_cliente.cpf}")
                        print(">> Cadastro NÃO efetuado! <<\n")
                    else:
                        grava_registro(novo_cliente)
                        print("Cliente cadastrado com sucesso!")

                elif opcao_2 == '2':
                    consulta_cpf = ""
                    while len(consulta_cpf) != 11 or not consulta_cpf.isdigit():
                        consulta_cpf = input("Digite o Cpf do cliente que deseja consultar: ")
                        if len(consulta_cpf) != 11 or not consulta_cpf.isdigit():
                            print("CPF inválido!")
                        else:
                            if cpf_ja_cadastrado(consulta_cpf):
                                print("\n::: Cliente localizado! :::")
                                print(localizar(clientes, 'cpf', consulta_cpf))
                            else:
                                print("\n::: Cliente NÃO localizado :::")

                            # cliente_encontrado = localizar(clientes, 'cpf', consulta_cpf)
                            # if cliente_encontrado is None:
                            #     print("\n::: Cliente NÃO localizado :::")
                            # else:
                            #     print("\n::: Cliente localizado! :::")
                            #     print(cliente_encontrado)

                elif opcao_2 == '3':
                    print("\n===== Listagem completa de clientes =====")
                    clientes = carrega_registros('clientes')
                    clientes.sort(key=lambda cliente: cliente.nome)
                    for cliente in clientes:
                        print(cliente)

            # Opção de Medicamentos Quimioterápicos
            elif opcao_1 == '2':
                if opcao_2 == '1':
                    novo_medicamento = cadastra_medicamento(fitoterapico=False)
                    grava_registro(novo_medicamento)

                elif opcao_2 == '2':
                    pass
                    # TO DO

                elif opcao_2 == '3':
                    print("\n===== Listagem completa de Medicamentos Quimioterápicos =====")
                    medicamentos = carrega_registros('medicamentos_quimi')
                    for med in medicamentos:
                        print(med)
                        print(' ========================== ')

            # Opção de Medicamentos Fitoterápicos
            elif opcao_1 == '3':
                if opcao_2 == '1':
                    novo_medicamento = cadastra_medicamento()
                    grava_registro(novo_medicamento)

                elif opcao_2 == '2':
                    pass
                    # TO DO

                elif opcao_2 == '3':
                    print("\n===== Listagem completa de Medicamentos Fitoterápicos =====")
                    medicamentos_fito = carrega_registros('medicamentos_fito')
                    for med in medicamentos_fito:
                        print(med)
                        print(' ========================== ')
                
        elif opcao_1 == '4': # Opção de Vendas
            opcao = '0'
            
            valor_total = 0
            lista_dos_medicamentos_vendidos = []
            cpf_venda = ""
            cliente_encontrado = ''
            while len(cpf_venda) != 11 or not cpf_venda.isdigit():
                cpf_venda = input("Digite o Cpf do cliente cadastrado: ")
                if len(cpf_venda) != 11 or not cpf_venda.isdigit():
                    print("CPF inválido!")
                else:
                    cliente_encontrado = localizar(carrega_registros('clientes'), 'cpf', cpf_venda)
                    if cliente_encontrado is None:
                        print("\n::: Cliente NÃO localizado :::")

                    elif cliente_encontrado is not None:
                        while opcao == '0':
                            opcao_venda = menu_vendas()
                            tipo_medicamento = 'medicamentos_quimi' if opcao_venda == '1' else 'medicamentos_fito'

                            medicamentos = carrega_registros(tipo_medicamento)
                            for medicamento in medicamentos:
                                print(medicamento)
                            print()
                            id_medicamento = input('Escolha o ID do medicamento que deseja incluir no carrinho: ')
                            medicamento_escolhido = localizar(medicamentos, 'id', id_medicamento)
                            
                            flag_continua_compra = True
                            if isinstance(medicamento_escolhido, MedicamentoQuimioterapico):
                                if medicamento_escolhido.necessita_receita is True:
                                    verificar_receita = input(f"ATENÇÃO! O medicamento '{medicamento.nome}' é de uso controlado. Você possui a receita? (S/N): ")
                                    if verificar_receita.upper() == "N":
                                        print("É necessario a receita do medicamento solicitado.")
                                        flag_continua_compra = False
                            
                            if flag_continua_compra is True:
                                qtd_medicamento = int(input('Digite a quantidade desejada: '))
                                valor_medicamento = medicamento.valor * qtd_medicamento
                                lista_dos_medicamentos_vendidos.append((medicamento.nome, str(qtd_medicamento), opcao_venda))
                                valor_total += valor_medicamento
                            
                            print()
                            opcao = input('Deseja adicionar outro medicamento: 1 - Sim ou 2 - Não: ')
                            print()
                            if opcao == '1':
                                opcao = '0'
                            else:
                                data = date.today().strftime('%d/%m/%Y')
                                hora = datetime.now().strftime("%H:%M:%S")
                                valor_com_desconto = calcular_desconto(valor_total, cliente_encontrado.data_de_nascimento)

                                venda = Venda(data,hora,lista_dos_medicamentos_vendidos, cliente_encontrado.cpf, valor_com_desconto)
                                print('Venda realizada com sucesso!! ')
                                print(venda)
                                grava_registro(venda)

                            # if opcao_venda == '1':
                            #     medicamentos_quimio = carrega_registros('medicamentos_quimi')           
                            #     for medicamento in medicamentos_quimio:
                            #         print(medicamento)
                            #     print()
                            #     id_medicamento = input('Escolha o ID do medicamento que deseja incluir no carrinho: ')
                            #     for medicamento in medicamentos_quimio:
                            #         if id_medicamento == medicamento.id:
                            #             if medicamento.necessita_receita == True:
                            #                 verificar_receita = input(f"ATENÇÃO! O medicamento '{medicamento.nome}' é de uso controlado. Você possui a receita? (S/N): ")
                            #                 if verificar_receita.upper() == "S":
                            #                     qtd_medicamento = int(input('Digite a quantidade desejada: '))
                            #                     valor_medicamento = 1 * qtd_medicamento
                            #                     lista_dos_medicamentos_vendidos.append(medicamento.nome) 
                            #                     valor_total += valor_medicamento
                            #                 else:
                            #                     print("É necessario a receita do medicamento solicitado.")
                            #             else:
                            #                 qtd_medicamento = int(input('Digite a quantidade desejada: '))
                            #                 valor_medicamento = medicamento.valor * qtd_medicamento
                            #                 lista_dos_medicamentos_vendidos.append((medicamento.nome, qtd_medicamento))
                            #                 valor_total += valor_medicamento
                            #     print()
                            #     opcao = input('Deseja adicionar outro medicamento: 1 - Sim ou 2 - Não: ')
                            #     print()
                            #     if opcao == '1':
                            #         opcao = '0'
                            #     else:
                            #         data = date.today().strftime('%d/%m/%Y')
                            #         hora = datetime.now().strftime("%H:%M:%S")
                            #         valor_com_desconto = calcular_desconto(valor_total, cliente_encontrado.data_de_nascimento)

                            #         venda = Venda(data,hora,lista_dos_medicamentos_vendidos, cliente_encontrado.cpf, valor_com_desconto)
                            #         print('Venda Realizada com sucesso!! ')
                            #         print(venda)
                            #         grava_registro(venda)

                            # elif opcao_venda == '2':
                            #     medicamentos_fito = carrega_registros('medicamentos_fito')
                            #     for medicamento in medicamentos_fito:
                            #         print(medicamento)
                            #     print()    
                            #     id_medicamento = input('Escolha o ID do medicamento que deseja incluir no carrinho: ')
                            #     for medicamento in medicamentos_fito:
                            #         if id_medicamento == medicamento.id:
                            #             qtd_medicamento = int(input('Digite a quantidade desejada: '))
                            #             valor_medicamento = medicamento.valor * qtd_medicamento
                            #             lista_dos_medicamentos_vendidos.append((medicamento.nome, qtd_medicamento))
                            #             valor_total += valor_medicamento
                                                    
                            #     print()
                            #     opcao = input('Deseja adicionar outro medicamento: 1 - Sim ou 2 - Não: ')
                            #     print()
                            #     if opcao == '1':
                            #         opcao = '0'
                            #     else:
                            #         data = date.today().strftime('%d/%m/%Y')
                            #         hora = datetime.now().strftime("%H:%M:%S")
                            #         calcular_desconto(valor_total, cliente_encontrado.data_de_nascimento)

                            #         venda = Venda(data,hora,lista_dos_medicamentos_vendidos, cliente_encontrado.cpf, valor_total)
                            #         print('Venda Realizada com sucesso!! ')
                            #         print(venda)
                            #         grava_registro(venda)


        elif opcao_1 == '5':
            for vendas in carrinho:
                print('Dentro do vendas 5')
                print(vendas)

        elif opcao_1 == '6':            
            emitir_relatorio_de_vendas()
            print("Execução finalizada!")
            break
        else:
            print('A opção escolhida é inválida!! ')


if __name__ == '__main__':
    main()
