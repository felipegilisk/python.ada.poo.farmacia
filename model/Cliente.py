from datetime import datetime, date
from typing import Any


class Cliente:
    """
    Classe modelo para o objeto Cliente, contendo os dados essenciais para tal: CPF, Nome e Data de Nascimento.

    Parameters:
        cpf (str): String contendo o CPF (11 ou 14 dígitos - não formatado e formatado, respectivamente).
        nome (str): String contendo o nome do Cliente a ser criado.
        data_nascimento (date | str): Objeto "date" ou "str" contendo a data de nascimento do Cliente.
    Returns:
        Cliente: Objeto do tipo Cliente, construído a partir dos parâmetros informados.
    """

    def __init__(self, cpf: str, nome: str, data_nascimento: date | str) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = self._formatar_data_nascimento(data_nascimento)
        self._idade = self._calcular_idade()

    @property
    def cpf(self) -> str:
        """
        Método GET para o atributo "cpf" do Cliente.

        Returns:
            str: String contendo o CPF do Cliente.
        """
        return self._cpf

    @property
    def nome(self) -> str:
        """
        Método GET para o atributo "nome" do Cliente.
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """
        Método SET para o atributo "nome" do Cliente.

        Parameters:
            nome (str): String contendo o novo valor a ser definido como nome.
        """
        self._nome = nome

    @property
    def data_nascimento(self) -> date:
        """
        Método GET para o atributo "data_nascimento" do Cliente.

        Returns:
            date: Objeto "date" contendo a data de nascimento do Cliente.
        """
        return self._data_nascimento

    @property
    def idade(self) -> int:
        """
        Método GET para o atributo "idade" do Cliente.

        Returns:
            date: Inteiro contendo a idade do Cliente.
        """
        return self._idade

    @staticmethod
    def _formatar_data_nascimento(data_nascimento: datetime | date | str) -> date:
        """
        Método para formatar automaticamente a data de nascimento informada para o objeto Cliente.

        Parameters:
            data_nascimento (date | str): Data de Nascimento em tipo "date" ou "str".

        Returns:
            date: Objeto "date" com a data de nascimento convertida para a tipagem correta.
        """
        if type(data_nascimento) is date:
            return data_nascimento
        if type(data_nascimento) is datetime:
            return data_nascimento.date()

        try:
            fmt_data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
        except (ValueError, TypeError):
            fmt_data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

        return fmt_data_nascimento

    def _calcular_idade(self) -> int:
        """
        Método para calcular automaticamente a idade com base na data de nascimento do Cliente.

        Returns:
            int: Valor Inteiro com a idade do Cliente.
        """
        ano_atual = date.today().year
        idade = ano_atual - self.data_nascimento.year
        if idade < 0:
            raise ValueError(f"A data de nascimento informada é inválida. Idade informada: {idade}.")

        return idade

    def __str__(self) -> str:
        """
        Override do método __str__ para a Classe Cliente.

        Returns:
            str: Informações do cliente formatadas para exibição.
        """
        str_fmt = (
            f"CPF:\t\t\t{self.cpf}\n"
            f"Nome:\t\t\t{self.nome}\n"
            f"Data de Nascimento:\t{self.data_nascimento.strftime('%d/%m/%Y')}\n"
            "------------------------------------------"
        )
        return str_fmt

    def __lt__(self, outro_cliente: Any) -> bool:
        """
        Override do método __lt__ para comparação entre dois objetos da Classe Cliente. Ordenação feita pelo nome.

        Returns:
            bool: True, se o nome da instância de Cliente atual vier antes do outro. False, caso contrário.
        """
        return self.nome < outro_cliente.nome

    def __dict__(self) -> dict:
        """
        Override do método __dict__ para recuperação dos dados do objeto Cliente em formato de dicionário.

        Returns:
            dict: Dados da classe Cliente formatados em dicionário.
        """
        fmt_dict = {
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.strftime("%Y-%m-%d")
        }
        return fmt_dict
