from datetime import date

class Cliente:
    """
    Classe para modelagem de objetos cliente
    """
    def __init__(self, cpf:str, nome:str, data_de_nascimento:date):
        self._cpf = cpf
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self,data_de_nascimento):
        self._data_de_nascimento = data_de_nascimento

    def __str__(self):
        """
        Definição do método string para a classe
        """
        return f"CPF:\t\t\t{self.cpf}\n"\
              f"Nome:\t\t\t{self.nome}\n"\
              f"Data de Nascimento:\t{self.data_de_nascimento.strftime('%d/%m/%Y')}\n"\
              "------------------------------------------"

    def __lt__(self, outro_cliente):
        """
        Definição do método comparativo entre 2 objetos, ordenando pelo nome
        """
        return self.nome < outro_cliente.nome


    def verifica_idade(self):
        data_agora = date.today()
        idade = data_agora.year - self.data_de_nascimento.year
        if data_agora.replace(year=self.data_de_nascimento.year) < self.data_de_nascimento:
            idade -= 1
        return idade
