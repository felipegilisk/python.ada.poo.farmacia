from datetime import date
from functions.relatorio import carrega_registros, localizar


def verifica_idade(data_de_nascimento: date):
    data_agora = date.today()
    idade = data_agora.year - data_de_nascimento.year
    if data_agora.replace(year=data_de_nascimento.year) < data_de_nascimento:
        idade -= 1

    return idade


def cpf_ja_cadastrado(cpf_a_consultar):
    clientes = carrega_registros('clientes')
    cliente_encontrado = localizar(clientes, 'cpf', cpf_a_consultar)
    
    return not cliente_encontrado is None


def calcular_desconto(valor_total, data_de_nascimento):
    if verifica_idade(data_de_nascimento) > 65:
        valor_total *= 0.8    

    elif valor_total > 150:
        valor_total *= 0.9
    return valor_total
