import csv
from datetime import datetime
from models.venda import Venda
from models.medicamento import MedicamentoVendido, MedicamentoFitoterapico, MedicamentoQuimioterapico
from models.cliente import Cliente
from models.laboratorio import Laboratorio


def ler_vendas(arquivo_csv):
    vendas = []

    with open(arquivo_csv, 'r', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader) 

        for row in reader:
            data = row[0]
            hora = row[1]
            produtos_vendidos = row[2]
            cliente = row[3]
            valor_total = float(row[4])
            
            vendas.append(Venda(data, hora, produtos_vendidos, cliente, valor_total))

    return vendas


def emitir_relatorio(vendas):
    medicamentos_vendidos = {}
    pessoas_atendidas = 0
    quimioterapicos_vendidos = {'quantidade': 0, 'valor': 0.0}
    fitoterapicos_vendidos = {'quantidade': 0, 'valor': 0.0}

    # for venda in vendas:
    #     produtos = venda.produtos_vendidos.split(',')
    #     pessoas_atendidas += 1

    #     for produto_str in produtos:  
    #         produto = produto_str.strip()  
    #         nome, quantidade, valor = produto.split('|')
    #         quantidade = int(quantidade)
    #         valor = float(valor)
    # for venda in vendas:
    #     produtos_str = venda.produtos_vendidos.strip('[]')  # Remover colchetes
    #     produtos = produtos_str.split(', ')
    #     pessoas_atendidas += 1

    #     for produto_str in produtos:
    #         produto = produto_str.strip("'")  # Remover aspas
    #         nome, quantidade, valor = produto.split('|')
    #         quantidade = int(quantidade)
    #         valor = float(valor)

    for venda in vendas:
        produtos_str = venda.produtos_vendidos.strip("[]")  # Remover colchetes
        produtos_list = produtos_str.split(", ")  # Dividir a string em uma lista de produtos

        pessoas_atendidas += 1

        # for produto_str in produtos_list:
        #     nome, quantidade, valor = produto_str.split('|')
        #     quantidade = int(quantidade)
        #     valor = float(valor)
        for produto_str in produtos:  # Renomeado para evitar conflito com variável anterior
          produto = produto_str.strip()  # Remover espaços em branco extras
          nome, quantidade, valor = produto.split('|')
          quantidade = int(quantidade)
          valor = float(valor)

          produtos = []  
          
        for produto in produtos_list:
            produto_sem_aspas = produto.strip("'")  # Remover aspas
            produtos.append(produto_sem_aspas)  # Adicionar o produto formatado à lista

        #pessoas_atendidas += 1
                
            if nome not in medicamentos_vendidos:
                medicamentos_vendidos[nome] = MedicamentoVendido(nome, quantidade, valor)
            else:
                medicamento = medicamentos_vendidos[nome]
                medicamento.quantidade += quantidade
                medicamento.valor_total += valor
            
            if nome.startswith('quimioterapico'):
                quimioterapicos_vendidos['quantidade'] += quantidade
                quimioterapicos_vendidos['valor'] += valor
            elif nome.startswith('fitoterapico'):
                fitoterapicos_vendidos['quantidade'] += quantidade
                fitoterapicos_vendidos['valor'] += valor

    relatorio_data = [
        ["Total de pessoas atendidas", pessoas_atendidas],
        ["Remédios quimioterápicos vendidos", quimioterapicos_vendidos['quantidade'], quimioterapicos_vendidos['valor']],
        ["Remédios fitoterápicos vendidos", fitoterapicos_vendidos['quantidade'], fitoterapicos_vendidos['valor']]
    ]

    medicamentos_data = [
        ["Nome", "Quantidade Vendida", "Valor Total Vendido"]
    ]

    for medicamento in sorted(medicamentos_vendidos.values(), key=lambda x: x.quantidade, reverse=True):
        medicamentos_data.append([medicamento.nome, medicamento.quantidade, medicamento.valor_total])

    with open('relatorio.csv', 'w', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(relatorio_data)
        writer.writerows([])  # Linha em branco para separar seções
        writer.writerows(medicamentos_data)

    # Impressão dos resultados
    # print("Relatório de Vendas")
    # print("===================")
    # print(f"Total de pessoas atendidas: {pessoas_atendidas}")
    # print(f"Remédios quimioterápicos vendidos: {quimioterapicos_vendidos['quantidade']} (Valor total: R${quimioterapicos_vendidos['valor']:.2f})")
    # print(f"Remédios fitoterápicos vendidos: {fitoterapicos_vendidos['quantidade']} (Valor total: R${fitoterapicos_vendidos['valor']:.2f})")
    
    # print("\nMedicamentos mais vendidos:")
    # for medicamento in sorted(medicamentos_vendidos.values(), key=lambda x: x.quantidade, reverse=True):
    #     print(f"{medicamento.nome}: Quantidade vendida: {medicamento.quantidade}, Valor total: R${medicamento.valor_total:.2f}")


def localizar(lista: list, chave, valor):
    """
    Método genérico para localizar um objeto na lista com base na chave fornecida
    Retorna None caso o objeto não seja encontrado
    """
    objeto_localizado = None
    for objeto in lista:
        if objeto.__getattribute__(chave) == valor:
            objeto_localizado = objeto

    return objeto_localizado


def carrega_registros(tipo: str):
    """
    Carrega os registros do tipo informado. Tipos conhecidos:
      - 'clientes'
      - 'medicamentos_quimi'
      - 'medicamentos_fito'
      - 'laboratorios'
      - 
    """
    if tipo not in ('clientes', 'medicamentos_quimi', 'medicamentos_fito', 'laboratorios', 'vendas'):
        lista = None
    else:
        lista = list()
        with open(f'./dados/{tipo}.csv', 'r', newline='', encoding="UTF-8") as meu_csv:
            leitor = csv.reader(meu_csv, delimiter=';')
            if tipo == 'clientes':
                for linha in leitor:
                    cliente = Cliente(linha[0], linha[1], datetime.strptime(linha[2], '%d/%m/%Y').date())
                    lista.append(cliente)
            elif tipo == 'laboratorios':
                for linha in leitor: 
                    lab = Laboratorio(linha[0], linha[1], linha[2], linha[3], linha[4])
                    lista.append(lab)
            elif tipo == 'medicamentos_fito':
                for linha in leitor:
                    med_fito = MedicamentoFitoterapico(linha[0], linha[1], linha[2], linha[3], linha[4], float(linha[5]))
                    lista.append(med_fito)
            elif tipo == 'medicamentos_quimi':
                for linha in leitor:
                    med_quimi = MedicamentoQuimioterapico(linha[0], linha[1], linha[2], linha[3], linha[4], float(linha[5]), True if linha[6] == 'S' else False)
                    lista.append(med_quimi)
            elif tipo == 'vendas':
                for linha in leitor:
                    venda = Venda(linha[0], linha[1], linha[2], linha[3], float(linha[4]))
                    lista.append(venda)
    return lista
