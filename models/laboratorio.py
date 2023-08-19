class Laboratorio:
    """
    Classe para modelagem de objetos do tipo Laboratorio
    """
    def __init__(self, id: str, nome:str, endereco:str, telefone:str, cidade:str, estado:str):
        self._id = id
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cidade = cidade
        self._estado = estado

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self,telefone):
        self._telefone = telefone

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self,cidade):
        self._cidade = cidade

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self,estado):
        self._estado = estado


    def __str__(self):
        texto = f"""::: Laboratório: {self.id} :::
        Nome:\t\t{self.nome}
        Endereço:\t{self.endereco}
        Telefone:\t{self.telefone}
        Cidade:\t\t{self.cidade}
        Estado:\t\t{self.estado}"""
        return texto
