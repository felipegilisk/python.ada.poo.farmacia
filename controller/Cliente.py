from datetime import datetime, date

from database.Core import FarmaciaFileDB
from model.Cliente import Cliente


class ClienteController:
    """
    Controladora responsável pelo gerenciamento de métodos relacionados a objetos Cliente.

    Parameters:
        database (FarmaciaFileDB): Instância ativa em memória da base de dados criada a partir do FileDB Engine.
    """
    def __init__(self, database: FarmaciaFileDB) -> None:
        self._db = database

    def recuperar_clientes(self, cpf: str | None = None) -> Cliente | tuple:
        if cpf is not None:
            fmt_cpf = self._format_cpf(u_cpf=cpf)
            cliente = self._db.search(
                target_db="clientes", target_field="cpf", search_value=fmt_cpf, lazy_mode=False
            )
            return cliente

        return tuple(self._db.read(target_db="clientes").values())

    @staticmethod
    def _format_cpf(u_cpf: str) -> str:
        """
        Método para formatação dos CPFs não formatados (apenas dígitos, 11 caracteres).

        Parameters:
            u_cpf (str): CPF não formatado (11 caracteres/digitos) a ser formatado.

        Returns:
            str: String contendo o CPF formatado, com 14 caracteres no total.
        """
        fmt_cpf = f"{u_cpf[:3]}.{u_cpf[3:6]}.{u_cpf[6:9]}-{u_cpf[9:11]}"
        return fmt_cpf

    def cadastrar_cliente(self) -> None:
        """
        Método para input, validação e criação de novos objetos da classe Cliente.
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

        self.check_cpf(cpf)
        cpf = self._format_cpf(u_cpf=cpf)

        data_nascimento = None
        while not isinstance(data_nascimento, date):
            data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            except (ValueError, TypeError):
                print("Data de nascimento inválida!")

        new_cliente = Cliente(cpf, nome, data_nascimento)
        self._db.write(data=new_cliente)

    def check_cpf(self, cpf: str) -> bool:
        """
        Método para verificar se um dado número de CPF está previamente cadastrado na base de dados.

        Parameters:
            cpf (str): String de 11 caracteres contendo o número do CPF não formatado a ser verificado.

        Returns:
            bool: True se o CPF for encontrado na base de dados. Caso contrário, False.
        """
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError(f"O CPF digitado para consulta é inválido.")

        fmt_cpf = self._format_cpf(u_cpf=cpf)
        cliente_encontrado = self._db.search(
            target_db="clientes", target_field="cpf", search_value=fmt_cpf, lazy_mode=False
        )
        if cliente_encontrado:
            print(cliente_encontrado.__str__())
            return True

        return False
