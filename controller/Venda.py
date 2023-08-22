from typing import List
from datetime import datetime

from model.Venda import Venda
from model.Medicamento import Medicamento
from model.Cliente import Cliente
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
        pessoas_atendidas = set()
        quimioterapicos_vendidos = []
        fitoterapicos_vendidos = []
        for venda in vendas.values():
            if venda.cliente not in pessoas_atendidas:
                pessoas_atendidas.add(venda.cliente.cpf)

            for produto in venda.produtos:
                med = self._db.search(
                    target_db="medicamentos", target_field="identificador",
                    search_value=produto.identificador, lazy_mode=False
                )
                qtdd = len([m for m in venda.produtos if m.identificador == produto.identificador])
                if produto.tipo_medicamento == "Q":  # quimio
                    if med not in [m['obj'] for m in quimioterapicos_vendidos]:
                        quimioterapicos_vendidos.append({'obj': med, 'qtdd': qtdd, 'valor_total': qtdd * med.valor})
                else:
                    if med not in [m['obj'] for m in fitoterapicos_vendidos]:
                        fitoterapicos_vendidos.append({'obj': med, 'qtdd': qtdd, 'valor_total': qtdd * med.valor})

        if len(fitoterapicos_vendidos) > 0:
            mais_vendido_f = sorted(fitoterapicos_vendidos, key=lambda x: x['qtdd'])[-1]
        else:
            fitoterapicos_vendidos.append({'obj': None, 'qtdd': 0, 'valor_total': 0})

        if len(quimioterapicos_vendidos) > 0:
            mais_vendido_q = sorted(quimioterapicos_vendidos, key=lambda x: x['qtdd'])[-1]
        else:
            quimioterapicos_vendidos.append({'obj': None, 'qtdd': 0, 'valor_total': 0})

        if mais_vendido_f['qtdd'] > mais_vendido_q['qtdd']:
            mais_vendido = mais_vendido_f
        else:
            mais_vendido = mais_vendido_q

        print(f""" ========== Relatório Final {datetime.today().strftime("%d/%m/%Y")} ==========\n
            Medicamento mais vendido:
            {mais_vendido['obj']}
            Quantidade: {mais_vendido['qtdd']}
            Valor Total: R$ {mais_vendido['valor_total']:.2f}

            * * * * * * * * * * * * * * * * *

            Quantidade de pessoas atendidas: {len(pessoas_atendidas)}

            * * * * * * * * * * * * * * * * *

            Quimioterápicos vendidos hoje:
            Quantidade: {sum([m['qtdd'] for m in quimioterapicos_vendidos])}
            Valor: R$ {sum([m['valor_total'] for m in quimioterapicos_vendidos]):.2f}

            * * * * * * * * * * * * * * * * *

            Fitoterápicos vendidos hoje:
            Quantidade: {sum([m['qtdd'] for m in fitoterapicos_vendidos])}
            Valor: R$ {sum([m['valor_total'] for m in fitoterapicos_vendidos]):.2f}
            """.replace('.', ','))
