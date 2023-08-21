from model.Laboratorio import Laboratorio


class Medicamento:
    """
        Classe modelo para o objeto Medicamento.

        Parameters:
            identificador (str): String contendo o idenficador do Medicamento.
            nome (str): String contendo o nome do Medicamento.
            principal_composto (str): String contendo o principal composto do Medicamento.
            laboratorio (Laboratorio): Objeto do tipo Laboratório associado ao Medicamento.
            descricao (str): String contendo a descrição do Medicamento.
            valor_unitario (float): Valor em ponto flutuante (Real) contendo o valor do Medicamento.
            receita_necessaria (bool): Booleano informando se a receita é necessária ou não para o Medicamento.
                                       Por padrão, é definido como False.
            tipo_medicamento (str): String informando qual o tipo de medicamento - Fito (F) ou Quimioterápico (Q).
        Returns:
            Medicamento: Objeto do tipo Medicamento, construído a partir dos parâmetros informados.
        """

    def __init__(
            self, identificador: str, nome: str, principal_composto: str, laboratorio: Laboratorio,
            descricao: str, valor_unitario: float, receita_necessaria: bool = False, tipo_medicamento: str = "F"
    ) -> None:
        self._identificador = identificador
        self._nome = nome
        self._principal_composto = principal_composto
        self._laboratorio = laboratorio
        self._descricao = descricao
        self._valor = valor_unitario
        self._receita_necessaria = receita_necessaria
        self._tipo_medicamento = tipo_medicamento

    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def principal_composto(self) -> str:
        return self._principal_composto

    @principal_composto.setter
    def principal_composto(self, principal_composto: str) -> None:
        self._principal_composto = principal_composto

    @property
    def laboratorio(self) -> Laboratorio:
        return self._laboratorio

    @laboratorio.setter
    def laboratorio(self, laboratorio: Laboratorio) -> None:
        self._laboratorio = laboratorio

    @property
    def descricao(self) -> str:
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        self._descricao = descricao

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self._valor = valor

    @property
    def receita_necessaria(self) -> bool:
        return self._receita_necessaria

    @receita_necessaria.setter
    def receita_necessaria(self, receita_necessaria: bool) -> None:
        self._receita_necessaria = receita_necessaria

    @property
    def tipo_medicamento(self) -> str:
        return self._tipo_medicamento

    @tipo_medicamento.setter
    def tipo_medicamento(self, tipo_medicamento: str) -> None:
        self._tipo_medicamento = tipo_medicamento

    def __str__(self):
        """
        Override do método __str__ para a Classe Medicamento.

        Returns:
            str: Informações do Medicamento formatadas para exibição.
        """
        receita_obr_str = "SIM" if self.receita_necessaria else "NÃO"
        valor_fmt_str = f"{self.valor:.2f}".replace(".", ",")
        nome_short = self.nome if len(self.nome) < 27 else f"{self.nome[:26]}..."
        tipo_short = "Quimio" if self.tipo_medicamento == "Q" else "Fito"

        fmt_str = (
            f"| {self.identificador :0>6} | {nome_short :^30} |"
            f"{receita_obr_str :^20} | R$ {valor_fmt_str :>11} | {tipo_short :^8} |"
        )
        return fmt_str

    def __dict__(self) -> dict:
        """
        Override do método __dict__ para recuperação dos dados do objeto Medicamento em formato de dicionário.

        Returns:
            dict: Dados da classe Medicamento formatados em dicionário.
        """
        fmt_dict = {
            "identificador": self.identificador,
            "nome": self.nome,
            "principal_composto": self.principal_composto,
            "laboratorio": self.laboratorio,
            "descricao": self.descricao,
            "valor_unitario": self.valor,
            "receita_necessaria": self.receita_necessaria,
            "tipo_medicamento": self.tipo_medicamento,
        }
        return fmt_dict
