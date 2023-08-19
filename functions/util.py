from datetime import date


def verifica_idade(data_de_nascimento: date):
    data_agora = date.today()
    idade = data_agora.year - data_de_nascimento.year
    if data_agora.replace(year=data_de_nascimento.year) < data_de_nascimento:
        idade -= 1

    # if data_de_nascimento.month > data_agora.month or (data_de_nascimento.month == data_agora.month and data_de_nascimento.day > data_agora.day):
    #     idade = data_agora.year - data_de_nascimento.year - 1
    # else:
    #     idade = data_agora.year - data_de_nascimento.year

    return idade
