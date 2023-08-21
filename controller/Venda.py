from typing import List
from datetime import datetime

from models.Venda import Venda
from models.Medicamento import Medicamento
from models.Cliente import Cliente
from database.Core import FarmaciaFileDB


class VendaController:
    """
    Controladora responsável pelo gerenciamento de métodos relacionados a objetos Venda.

    Parameters:
        database (FarmaciaFileDB): Instância ativa em memória da base de dados criada a partir do FileDB Engine.
    """
    def __init__(self, database: FarmaciaFileDB) -> None:
        self._db = database

    def registar_venda(self, produtos: List[Medicamento], cliente: Cliente):
        momento_venda = datetime.now()

        nova_venda = Venda(momento_venda, produtos, cliente)
        self._db.write(data=nova_venda)

        nova_venda.__str__()
        print('Venda realizada com sucesso!! ')

    def emitir_relatorio_de_vendas(self) -> None:
        """
        Método responsável pela emissão do relatório das Vendas realizadas dentro do sistema.
        """
        vendas = self._db.read(target_db="vendas")
        pessoas_atendidas = []
        medicamentos_vendidos = []
        for venda in vendas:
            produtos_ids = vendas["produto_ids"]
            produtos = [
                produto for produto in [
                    self._db.search(
                        target_db="medicamentos", target_field="identificador", search_value=prod_id, lazy_mode=False
                    ) for prod_id in produtos_ids
                ]
            ]
            if venda.cliente not in pessoas_atendidas:
                pessoas_atendidas.append(venda.cliente)

            for med in produtos:
                qtdd = 0
                if med not in medicamentos_vendidos:
                    medicamentos_vendidos.append({'obj': med, 'qtdd': qtdd, 'valor_total': qtdd * med.valor})
                else:
                    i = [m['obj'] for m in medicamentos_vendidos].index(med)
                    medicamentos_vendidos[i]['qtdd'] += qtdd
                    medicamentos_vendidos[i]['valor_total'] += qtdd * med.valor

        if len(medicamentos_vendidos) > 0:
            mais_vendido = sorted(medicamentos_vendidos, key=lambda x: x['qtdd'])[-1]
        else:
            mais_vendido = {'obj': None, 'qtdd': 0, 'valor_total': 0}

        print(f""" ========== Relatório Final {datetime.today().strftime("%d/%m/%Y")} ==========\n
        Medicamento mais vendido:
        {mais_vendido['obj']}
        Quantidade: {mais_vendido['qtdd']}
        Valor Total: R$ {mais_vendido['valor_total']:.2f}

        * * * * * * * * * * * * * * * * *

        Quantidade de pessoas atendidas: {len(pessoas_atendidas)}

        * * * * * * * * * * * * * * * * *

        Medicamentos vendidos hoje:
        Quantidade: {sum([m['qtdd'] for m in medicamentos_vendidos])}
        Valor: R$ {sum([m['valor_total'] for m in medicamentos_vendidos]):.2f}
        Tipo: 
        """.replace('.', ','))
