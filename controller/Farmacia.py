from database.Core import FarmaciaFileDB
from controller.Cliente import ClienteController
from controller.Medicamento import MedicamentoController
from controller.Venda import VendaController


class FarmaciaController:
    """
    Classe responsável por servir como Controladora-Central para as demais três controladoras disponíveis para
    o sistema. Também centraliza a instância do FileDB Engine para acesso compartilhado das controladoras.
    """
    def __init__(self) -> None:
        self._database = FarmaciaFileDB()
        self._user_ctl = ClienteController(database=self._database)
        self._drug_ctl = MedicamentoController(database=self._database)
        self._sell_ctl = VendaController(database=self._database)

    @property
    def user_controller(self) -> ClienteController:
        """
        Método GET para acesso ao Controlador de Usuários.

        Returns:
            ClienteController: Controlador do sistema para Usuários.
        """
        return self._user_ctl

    @property
    def drug_controller(self) -> MedicamentoController:
        """
        Método GET para acesso ao Controlador de Medicamentos.

        Returns:
            MedicamentoController: Controlador do sistema para Medicamentos.
        """
        return self._drug_ctl

    @property
    def sell_controller(self) -> VendaController:
        """
        Método GET para acesso ao Controlador de Vendas.

        Returns:
            VendaController: Controlador do sistema para Vendas.
        """
        return self._sell_ctl
