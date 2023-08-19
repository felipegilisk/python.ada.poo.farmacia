
class Venda:
    """
    Classe para modelagem de objetos do tipo Vendas
    """
    def __init__(self, data:str, hora:str, produtos_vendidos:list, cliente:str, valor_total:float):
        self._data = data
        self._hora = hora
        self._produtos_vendidos = produtos_vendidos
        self._cliente = cliente
        self._valor_total = valor_total

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,data):
        self._data = data

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self,hora):
        self._hora = hora

    @property
    def produtos_vendidos(self):
        return self._produtos_vendidos

    @produtos_vendidos.setter
    def produtos_vendidos(self, produtos_vendidos):
        self._produtos_vendidos = produtos_vendidos

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self,cliente):
        self._cliente = cliente

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self,valor_total):
        self._valor_total = valor_total

    def __str__(self):
        """
        Definição do método string para a classe
        """
        return f"Data da venda:\t\t\t{self.data}\n"\
              f"Hora da venda:\t\t\t{self.hora}\n"\
              f"Produtos vendidos:\t\t{self.produtos_vendidos}\n"\
              f"Cpf do cliente:\t\t\t{self.cliente}\n"\
              f"Valor total da compra:\t\tR$ {self.valor_total:.2f}\n"\
              "------------------------------------------".replace('.', ',')
