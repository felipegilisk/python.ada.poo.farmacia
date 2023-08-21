from datetime import datetime
from typing import List

from model.Cliente import Cliente
from model.Medicamento import Medicamento


class Venda:
    """
    Classe modelo para o objeto Venda.

    Parameters:
        momento_venda (str): Objeto do tipo "datetime" referente ao período da Venda (data + hora).
        produtos (List[Medicamento]): Lista de objetos da classe Medicamento relacionados aos itens vendidos.
        cliente (Cliente): Objeto da classe Cliente referente ao cliente relacionado a Venda.
    Returns:
        Venda: Objeto do tipo Venda, construído a partir dos parâmetros informados.
    """

    def __init__(self, momento_venda: datetime, produtos: List[Medicamento], cliente: Cliente) -> None:
        self._momento_venda = momento_venda
        self._cliente = cliente
        self._produtos = produtos
        self._valor_venda = self._calcular_valor_total()

    @property
    def momento_venda(self) -> datetime:
        """
        Método GET para o parâmetro "momento_venda".

        Returns:
            datetime: Período (Data/Hora) em que a venda foi efetivada.
        """
        return self._momento_venda

    @property
    def cliente(self) -> Cliente:
        """
        Método GET para o parâmetro "cliente".

        Returns:
            Cliente: Objeto da classe Cliente contendo o cliente associado a Venda.
        """
        return self._cliente

    @property
    def produtos(self) -> List[Medicamento]:
        """
        Método GET para o parâmetro "produtos".

        Returns:
            List[Medicamento]: Lista contendo os produtos da classe Medicamento associados a Venda.
        """
        return self._produtos

    @produtos.setter
    def produtos(self, produtos: List[Medicamento]) -> None:
        """
        Método SET para o parâmetro "produtos". Também atualiza o valor total da venda a partir dos novos produtos.

        Parameters:
            produtos (List[Medicamento]): Nova lista com os objetos da classe Medicamento a serem inseridos na Venda.
        """
        self._produtos = produtos
        self._valor_venda = self._calcular_valor_total()

    @property
    def valor_venda(self) -> float:
        """
        Método GET para o parâmetro "valor_venda".

        Returns:
            float: Valor total da Venda efetivada com base na lista de produtos com objetos da classe Medicamento.
        """
        return self._valor_venda

    def _calcular_valor_total(self) -> float:
        """
        Método para calcular o valor total da venda efetivada com base na lista de produtos composta por objetos da
        classe Medicamento.

        Returns:
            float: Somatório do valor dos produtos inclusos no parâmetro "produtos", com o desconto de venda aplicado.
        """
        valor_total = 0.0
        if len(self.produtos) > 0:
            for produto in self.produtos:
                valor_total += produto.valor

        valor_desconto = self._calcular_desconto(valor_total=valor_total)
        return valor_desconto

    def _calcular_desconto(self, valor_total: float) -> float:
        """
        Método responsável pelo cálculo de descontos no valor total a partir da idade do Cliente.

        Parameters:
            valor_total (float): Valor total da venda a ser utilizado para o cálculo.

        Returns:
            float: Valor final da venda com o desconto proporcional as regras de idade aplicadas.
        """
        if self.cliente.idade > 65:
            valor_total *= 0.8
        elif valor_total > 150:
            valor_total *= 0.9

        return valor_total

    def __str__(self) -> str:
        """
        Override do método __str__ para a Classe Venda.

        Returns:
            str: Informações da Venda formatadas para exibição.
        """
        valor_fmt_str = f"{self._valor_venda:.2f :>8}".replace('.', ',')
        data_hora_venda = self.momento_venda.date().strftime("%d/%m/%y %H:%M:%S")
        produtos_str = "".join([produto.__str__() for produto in self.produtos])

        fmt_str = (
            "|-----------------------------------------------------------------------------------------|\n"
            "|----------------------------------- Detalhes da Venda -----------------------------------|\n"
            "|-----------------------------------------------------------------------------------------|\n"
            "|                                         Cliente                                         |\n"
            "|-----------------------------------------------------------------------------------------|\n"
            f"| CPF: {self.cliente.cpf :<49} Data/Hora: {data_hora_venda} |\n"
            "|-----------------------------------------------------------------------------------------|\n"
            "|                                    Produtos Vendidos                                    |\n"
            "|-----------------------------------------------------------------------------------------|\n"
            "|   ID   |              Nome              | Receita Obrigatória | Valor Unitário |   Tipo   |\n"
            f"{produtos_str}"
            "|                                                                              |          |\n"
            f"|------------------------------------------------------- TOTAL: R$ {valor_fmt_str} |----------|\n"
        )

        return fmt_str

    def __dict__(self) -> dict:
        """
        Override do método __dict__ para recuperação dos dados do objeto Venda em formato de dicionário.

        Returns:
            dict: Dados da classe Venda formatados em dicionário.
        """
        fmt_dict = {
            "momento_venda": self.momento_venda.strftime("%Y-%m-%d %H:%M:%S"),
            "cliente": self.cliente.cpf,
            "valor_venda": self.valor_venda,
            "produto_ids": [produto.identificador for produto in self.produtos]
        }
        return fmt_dict
