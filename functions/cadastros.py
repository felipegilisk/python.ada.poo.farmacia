import csv
from datetime import datetime, date
from models.cliente import Cliente
from models.medicamento import MedicamentoFitoterapico, MedicamentoQuimioterapico
from models.laboratorio import Laboratorio
from models.venda import Venda
from functions.relatorio import carrega_registros


def cadastros_iniciais():
    """
    Cria os cadastros iniciais de clientes, medicamentos e laboratorios
    """
    with open('./dados/clientes.csv', 'w', newline='', encoding="UTF-8") as meu_csv:
        escritor = csv.writer(meu_csv, delimiter=';')
        escritor.writerow(['10010010017', 'Helena', '20/01/2001'])
        escritor.writerow(['20020020023', 'Patrícia', '20/02/2002'])
        escritor.writerow(['30030030030', 'Gabriel', '20/03/2003'])
        escritor.writerow(['40040040046', 'Francisco', '20/04/2004'])
        escritor.writerow(['50050050050', 'Wesley', '15/12/1939'])
        escritor.writerow(['60060060060', 'Gislaine', '31/10/1950'])

    with open('./dados/laboratorios.csv', 'w', newline='', encoding="UTF-8") as meu_csv:
        escritor = csv.writer(meu_csv, delimiter=';')
        escritor.writerow(['1', 'Bryo', '11975546464', 'Avenida Cem, S/N', 'Serra', 'ES'])
        escritor.writerow(['2', 'TheraSkin', '08000196660', 'Marginal Direita da, Rod. Anchieta, Km 13,5', 'Rudge Ramos', 'SP'])
        escritor.writerow(['3', 'Baxter', '1156350106', 'Avenida Engenheiro Eusébio Stevaux, 2555', 'São Paulo', 'SP'])
        escritor.writerow(['4', 'Bristol-Myers Squibb', '08007276160', 'Rua Verbo Divino, 1711', 'São Paulo', 'SP'])
        escritor.writerow(['5', 'PROCTER & GAMBLE', '1137480327', 'Av. Maria Coelho Aguiar, 215', 'São Paulo', 'SP'])
        escritor.writerow(['6', 'Farmacam', '2126051349', 'Rua Coronel Serrado, 1630', 'São Gonçalo', 'RJ'])
        escritor.writerow(['7', 'EUROFARMA', '08007043876', 'Rua Brito Peixoto, 554', 'São Paulo', 'SP'])

    with open('./dados/medicamentos_fito.csv', 'w', newline='', encoding="UTF-8") as meu_csv:
        escritor = csv.writer(meu_csv, delimiter=';')
        escritor.writerow([1,'Camomilina', 'Camomila', 'TheraSkin', 'Cicatrizante com ação anti-inflamatória', '20.30'])
        escritor.writerow([2,'Vick Vaporub', 'Eucalipto', 'PROCTER & GAMBLE', 'Expectorante e broncodilatador', '14.99'])
        escritor.writerow([3,'Casca de Salgueiro Branco', 'Salgueiro', 'Farmacam', 'Alivio das articulações e conforto muscular', '10.15'])
        escritor.writerow([4,'Aloe vera extrato', 'Babosa', 'Bryo', 'Cicatrizante com ação anti-inflamatória','11.00'])

    with open("./dados/medicamentos_quimi.csv", 'w', newline='', encoding="UTF-8") as meu_csv:
        escritor = csv.writer(meu_csv, delimiter=';')
        escritor.writerow([1,'Genuxal', 'Ciclofosfamida', 'Baxter', 'Tratamento de tumores malígnos e doenças do sistema imunológico', '69.00', 'S'])
        escritor.writerow([2,'Taxol', 'Paclitaxel', 'Bristol-Myers Squibb', 'Tratamento adjuvante do câncer de mama linfonodo positivo', '81.00', 'N'])
        escritor.writerow([3,'Gemzar', 'Cloridrato de gencitabina', 'EUROFARMA', 'Tratamento de pacientes com câncer de bexiga e adenocarcinoma do pâncreas', '413.00', 'S'])
        escritor.writerow([4,'Norelbin', 'Vinorelbina', 'EUROFARMA', 'Tratamento de recidiva de câncer de mama', '186.00', 'N'])

    with open("./dados/vendas.csv", 'w', newline='', encoding="UTF-8") as meu_csv:
        escritor = csv.writer(meu_csv, delimiter=';')


def cadastra_cliente():
    """
    Função para validações dos atributos do cliente
    Após validados, retorna um objeto da classe Cliente
    """
    nome = ""
    while len(nome) == 0:
      nome = input("Digite o nome do cliente: ")
      if len(nome) == 0:
        print("Nome inválido!")

    cpf = ""
    while len(cpf) != 11 or not cpf.isdigit():
      cpf = input("Digite o CPF do cliente (somente números): ")
      if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido!")

    data_de_nascimento = None
    while not isinstance(data_de_nascimento, date):
      data_de_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
      try:
        data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
      except:
        print("Data de nascimento inválida!")

    return Cliente(cpf, nome, data_de_nascimento)


def cadastra_medicamento(fitoterapico: bool= True):
    """
    Método para cadastro de medicamentos fitoterapicos e quimioterapicos
    """

    # id = ""
    # while len(id) == 0:
    #   id = input("Digite o id do medicamento: ")
    #   if len(id) == 0:
    #     print("Id inválido!")

    nome = ""
    while len(nome) == 0:
      nome = input("Digite o nome do medicamento: ")
      if len(nome) == 0:
        print("Nome inválido!")

    principal_composto = ""
    while len(principal_composto) == 0:
      principal_composto = input("Digite o principal composto do medicamento: ")
      if len(principal_composto) == 0:
        print("Composto inválido")

    laboratorio = 'null'
    labs = carrega_registros('laboratorios')
    labs_nomes = [lab.nome for lab in labs]
    for lab in labs:
       print(lab)
       print("- - - - - - - - - - - - - - - - ")
    while laboratorio not in labs_nomes:
       laboratorio = input("Digite o nome do laboratório: ")
       if laboratorio not in labs_nomes:
          print("Nome inválido!")

    descricao = ""
    while len(descricao) == 0:
      descricao = input("Digite a descrição do medicamento: ")
      if len(descricao) == 0:
        print("Descrição inválida")

    valor = ""
    while len(valor) == 0:
      valor = input("Digite o valor do medicamento: ")
      if len(valor) == 0:
        print("Valor inválido!")

    if fitoterapico is True:
        id = 0
        medicamentos_fitoterapicos = carrega_registros('medicamentos_fito')
        for medicamento in medicamentos_fitoterapicos:
            id = int(medicamento.id[-1]) + 1
        print(f"Medicamento Fitoterápico cadastrado com sucesso! Código: {id}")
        return MedicamentoFitoterapico(id,nome, principal_composto, laboratorio, descricao, valor)

    else:
        necessita_receita = input('O remédio necessita de receita? Digite S para Sim ou N para Não: ')
        id = 0
        medicamentos_quimioterapicos = carrega_registros('medicamentos_quimi')
        for medicamento in medicamentos_quimioterapicos:
            id = int(medicamento.id[-1]) + 1
        print(f"Medicamento Quimioterápico cadastrado com sucesso! Código: {id}")
        return MedicamentoQuimioterapico(id, nome, principal_composto, laboratorio, descricao, valor, necessita_receita.upper())


def grava_registro(obj):
    """
    Guarda os dados do objeto novo no respectivo arquivo
    """
    if isinstance(obj, Cliente):
        with open('./dados/clientes.csv', 'a', newline='', encoding="UTF-8") as meu_csv:
            escritor = csv.writer(meu_csv, delimiter=';')
            escritor.writerow([obj.cpf, obj.nome, obj.data_de_nascimento.strftime('%d/%m/%Y')])

    elif isinstance(obj, Laboratorio):
        with open('./dados/laboratorios.csv', 'a', newline='', encoding="UTF-8") as meu_csv:
            escritor = csv.writer(meu_csv, delimiter=';')
            escritor.writerow([obj.nome, obj.telefone, obj.endereco, obj.cidade, obj.estado])

    elif isinstance(obj, MedicamentoFitoterapico):    
        with open('./dados/medicamentos_fito.csv', 'a', newline='', encoding="UTF-8") as meu_csv:
            escritor = csv.writer(meu_csv, delimiter=';')
            escritor.writerow([obj.id,obj.nome, obj.principal_composto, obj.laboratorio, obj.descricao, obj.valor])

    elif isinstance(obj, MedicamentoQuimioterapico):
        with open('./dados/medicamentos_quimi.csv', 'a', newline='', encoding="UTF-8") as meu_csv:
            escritor = csv.writer(meu_csv, delimiter=';')
            escritor.writerow([obj.id,obj.nome, obj.principal_composto, obj.laboratorio, obj.descricao, obj.valor, 'S' if obj.necessita_receita else 'N'])
    
    elif isinstance(obj, Venda):
        with open('./dados/vendas.csv', 'a', newline='', encoding="UTF-8") as meu_csv:
            escritor = csv.writer(meu_csv, delimiter=';')
            escritor.writerow([obj.data, obj.hora, obj.produtos_vendidos, obj.cliente, str(obj.valor_total)])
    
    else:
       raise TypeError("Tipo de dado desconhecido!")

    print("Registro salvo com sucesso!")
