class Laboratorio:
    """
    Classe modelo para o objeto Laboratorio.

    Parameters:
        nome (str): String contendo o nome do Laboratório a ser criado.
        endereco (str): String contendo o endereço do Laboratório.
        telefone (str): String contendo o telefone do Laboratório.
        cidade (str): String contendo a cidade do Laboratório.
        estado (str): String contendo o estado do Laboratório.
    Returns:
        Laboratorio: Objeto do tipo Laboratorio, construído a partir dos parâmetros informados.
    """

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cidade = cidade
        self._estado = estado

    @property
    def nome(self) -> str:
        """
        Método GET para o parâmetro "nome" do Laboratório.

        Returns:
            str: Nome atribuído ao Laboratório.
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """
        Método SET para o parâmetro "nome" do Laboratório.

        Parameters:
            nome (str): Novo nome a ser atribuído ao Laboratório.
        """
        self._nome = nome

    @property
    def endereco(self) -> str:
        """
        Método GET para o parâmetro "endereco" do Laboratório.

        Returns:
            str: Endereço atribuído ao Laboratório.
        """
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        """
        Método SET para o parâmetro "endereco" do Laboratório.

        Parameters:
            endereco (str): Novo endereco a ser atribuído ao Laboratório.
        """
        self._endereco = endereco

    @property
    def telefone(self) -> str:
        """
        Método GET para o parâmetro "telefone" do Laboratório.

        Returns:
            str: Telefone atribuído ao Laboratório.
        """
        return self._telefone

    @telefone.setter
    def telefone(self, telefone) -> None:
        """
        Método SET para o parâmetro "telefone" do Laboratório.

        Parameters:
            telefone (str): Novo telefone a ser atribuído ao Laboratório.
        """
        self._telefone = telefone

    @property
    def cidade(self) -> str:
        """
        Método GET para o parâmetro "cidade" do Laboratório.

        Returns:
            str: Cidade atribuída ao Laboratório.
        """
        return self._cidade

    @cidade.setter
    def cidade(self, cidade: str) -> None:
        """
        Método SET para o parâmetro "cidade" do Laboratório.

        Parameters:
            cidade (str): Nova cidade a ser atribuída ao Laboratório.
        """
        self._cidade = cidade

    @property
    def estado(self) -> str:
        """
        Método GET para o parâmetro "estado" do Laboratório.

        Returns:
            str: Estado atribuído ao Laboratório.
        """
        return self._estado

    @estado.setter
    def estado(self, estado: str) -> None:
        """
        Método SET para o parâmetro "estado" do Laboratório.

        Parameters:
            estado (str): Novo estado a ser atribuído ao Laboratório.
        """
        self._estado = estado

    def __str__(self) -> str:
        """
        Override do método __str__ para a Classe Laboratorio.

        Returns:
            str: Informações do Laboratório formatadas para exibição.
        """
        str_fmt = (
            f"::: Laboratório: {self.nome} :::"
            f"Endereço:\t{self.endereco}"
            f"Telefone:\t{self.telefone}"
            f"Cidade:\t\t{self.cidade}"
            f"Estado:\t\t{self.estado}"
        )
        return str_fmt

    def __dict__(self) -> dict:
        """
        Override do método __dict__ para recuperação dos dados do objeto Laboratorio em formato de dicionário.

        Returns:
            dict: Dados da classe Laboratorio formatados em dicionário.
        """
        fmt_dict = {
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "estado": self.estado
        }
        return fmt_dict
