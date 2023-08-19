"""
Classes Medicamento, MedicamentoFitoterápico e MedicamentoQuimioterápico
"""

class Medicamento:
    """
    Classe mãe para as classes MedicamentoQuimioterapico e MedicamentoFitoterapico
    """
    def __init__(self,id: str, nome:str, principal_composto:str, laboratorio:str, descricao:str, valor:float):
        self._id = id
        self._nome = nome
        self._principal_composto = principal_composto
        self._laboratorio = laboratorio
        self._descricao = descricao
        self._valor = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def principal_composto(self):
        return self._principal_composto

    @principal_composto.setter
    def principal_composto(self,principal_composto):
        self._principal_composto = principal_composto

    @property
    def laboratorio(self):
        return self._laboratorio

    @laboratorio.setter
    def laboratorio(self,laboratorio):
        self._laboratorio = laboratorio

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self,descricao):
        self._descricao = descricao

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
      self._valor = valor


class MedicamentoQuimioterapico(Medicamento):
    """
    Classe para modelagem de objetos deste tipo de medicamento
    Está é uma classe filha da classe Medicamento
    """
    def __init__(self,id: str,nome:str, principal_composto:str, laboratorio:str, descricao:str, valor:float, necessita_receita:bool):
        super().__init__(id, nome, principal_composto, laboratorio, descricao, valor)
        self._necessita_receita = necessita_receita

    @property
    def necessita_receita(self):
        return self._necessita_receita

    @necessita_receita.setter
    def necessita_receita(self,necessita_receita):
        self._necessita_receita = necessita_receita
    
    def __str__(self):
        return f'{self.id} - {self.nome} - Necessidade de receita: {self.necessita_receita} - R$ {self.valor:.2f}'.replace('.', ',')


class MedicamentoFitoterapico(Medicamento):
    """
    Classe para modelagem de objetos deste tipo de medicamento
    Está é uma classe filha da classe Medicamento
    """
    def __init__(self,id: str,nome:str, principal_composto:str, laboratorio:str, descricao:str, valor:float):
        super().__init__(id,nome, principal_composto, laboratorio, descricao, valor)

    def __str__(self):
        return f'{self.id} - {self.nome} - R$ {self.valor:.2f}'.replace('.', ',')


class MedicamentoVendido:
    def __init__(self, nome, quantidade, valor_total):
        self.nome = nome
        self.quantidade = quantidade
        self.valor_total = valor_total
