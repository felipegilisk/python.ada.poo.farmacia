import csv
from datetime import datetime
from models.cliente import Cliente
from models.medicamento import MedicamentoFitoterapico, MedicamentoQuimioterapico, MedicamentoVendido
from models.laboratorio import Laboratorio
from models.venda import Venda


def emitir_relatorio_de_vendas():
    vendas = carrega_registros('vendas')
    pessoas_atendidas = list()
    quimioterapicos_vendidos = list()
    # [{'obj': medicamento, 'quantidade': 0, 'valor_total': 0}]
    fitoterapicos_vendidos = list()

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
        produtos_str = venda.produtos_vendidos
        aux = produtos_str[2:-2].split('), (')
        produtos_list = [item[1:-1].split("', '") for item in aux]

        if venda.cliente not in pessoas_atendidas:
            pessoas_atendidas.append(venda.cliente)

        for produto in produtos_list:
            if produto[2] == '1': # quimio
                med = localizar(carrega_registros('medicamentos_quimi'), 'nome', produto[0])
                qtdd = int(produto[1])
                if med not in [m['obj'] for m in quimioterapicos_vendidos]:
                    quimioterapicos_vendidos.append({'obj': med, 'qtdd': qtdd, 'valor_total': qtdd*med.valor})
                else:
                    i = [m['obj'] for m in quimioterapicos_vendidos].index(med)
                    quimioterapicos_vendidos[i]['qtdd'] += qtdd
                    quimioterapicos_vendidos[i]['valor_total'] += qtdd*med.valor

            elif produto[2] == '2': # fito
                med = localizar(carrega_registros('medicamentos_fito'), 'nome', produto[0])
                qtdd = int(produto[1])
                if med not in [m['obj'] for m in fitoterapicos_vendidos]:
                    fitoterapicos_vendidos.append({'obj': med, 'qtdd': qtdd, 'valor_total': qtdd*med.valor})
                else:
                    i = [m['obj'] for m in fitoterapicos_vendidos].index(med)
                    fitoterapicos_vendidos[i]['qtdd'] += qtdd
                    fitoterapicos_vendidos[i]['valor_total'] += qtdd*med.valor

    if len(fitoterapicos_vendidos) > 0:
        mais_vendido_f = sorted(fitoterapicos_vendidos, key=lambda x: x['qtdd'])[-1]
    else:
        fitoterapicos_vendidos.append({'obj': None, 'qtdd': 0, 'valor_total': 0})

    if len(quimioterapicos_vendidos) > 0:
        mais_vendido_q = sorted(quimioterapicos_vendidos, key=lambda x: x['qtdd'])[-1]
    else:
        quimioterapicos_vendidos.append({'obj': None, 'qtdd': 0, 'valor_total': 0})

    if mais_vendido_f['qtdd'] > mais_vendido_q['qtdd']:
        mais_vendido = mais_vendido_f
    else:
        mais_vendido = mais_vendido_q

    print(f""" ========== Relatório Final {datetime.today().strftime("%d/%m/%Y")} ==========\n
    Medicamento mais vendido:
    {mais_vendido['obj']}
    Quantidade: {mais_vendido['qtdd']}
    Valor Total: R$ {mais_vendido['valor_total']:.2f}

    * * * * * * * * * * * * * * * * *

    Quantidade de pessoas atendidas: {len(pessoas_atendidas)}

    * * * * * * * * * * * * * * * * *

    Quimioterápicos vendidos hoje:
    Quantidade: {sum([m['qtdd'] for m in quimioterapicos_vendidos])}
    Valor: R$ {sum([m['valor_total'] for m in quimioterapicos_vendidos]):.2f}

    * * * * * * * * * * * * * * * * *

    Fitoterápicos vendidos hoje:
    Quantidade: {sum([m['qtdd'] for m in fitoterapicos_vendidos])}
    Valor: R$ {sum([m['valor_total'] for m in fitoterapicos_vendidos]):.2f}
    """.replace('.', ','))

        # for produto_str in produtos_list:
        #     nome, quantidade, valor = produto_str.split('|')
        #     quantidade = int(quantidade)
        #     valor = float(valor)
        # for produto_str in produtos:  # Renomeado para evitar conflito com variável anterior
        #   produto = produto_str.strip()  # Remover espaços em branco extras
        #   nome, qtdd, valor = produto.split('|')
        #   qtdd = int(qtdd)
        #   valor = float(valor)

        #   produtos = []  
          
        # for produto in produtos_list:
        #     produto_sem_aspas = produto.strip("'")  # Remover aspas
        #     produtos.append(produto_sem_aspas)  # Adicionar o produto formatado à lista

        # #pessoas_atendidas += 1
                
        #     if nome not in medicamentos_vendidos:
        #         medicamentos_vendidos[nome] = MedicamentoVendido(nome, qtdd, valor)
        #     else:
        #         medicamento = medicamentos_vendidos[nome]
        #         medicamento.quantidade += qtdd
        #         medicamento.valor_total += valor
            
        #     if nome.startswith('quimioterapico'):
        #         quimioterapicos_vendidos['quantidade'] += qtdd
        #         quimioterapicos_vendidos['valor'] += valor
        #     elif nome.startswith('fitoterapico'):
        #         fitoterapicos_vendidos['quantidade'] += qtdd
        #         fitoterapicos_vendidos['valor'] += valor

    # relatorio_data = [
    #     ["Total de pessoas atendidas", pessoas_atendidas],
    #     ["Remédios quimioterápicos vendidos", quimioterapicos_vendidos['quantidade'], quimioterapicos_vendidos['valor']],
    #     ["Remédios fitoterápicos vendidos", fitoterapicos_vendidos['quantidade'], fitoterapicos_vendidos['valor']]
    # ]

    # medicamentos_data = [
    #     ["Nome", "Quantidade Vendida", "Valor Total Vendido"]
    # ]

    # for medicamento in sorted(medicamentos_vendidos.values(), key=lambda x: x.quantidade, reverse=True):
    #     medicamentos_data.append([medicamento.nome, medicamento.quantidade, medicamento.valor_total])

    # with open('relatorio.csv', 'w', newline='', encoding='UTF-8') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerows(relatorio_data)
    #     writer.writerows([])  # Linha em branco para separar seções
    #     writer.writerows(medicamentos_data)

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
      - 'vendas'
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
                    lab = Laboratorio(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
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
