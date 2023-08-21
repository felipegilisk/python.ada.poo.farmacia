from database.Core import FarmaciaFileDB
from models.Medicamento import Medicamento


class MedicamentoController:
    """
    Controladora responsável pelo gerenciamento de métodos relacionados a objetos Medicamento.

    Parameters:
        database (FarmaciaFileDB): Instância ativa em memória da base de dados criada a partir do FileDB Engine.
    """
    def __init__(self, database: FarmaciaFileDB) -> None:
        self._db = database

    def recuperar_medicamentos(self, identificador: str | None = None) -> Medicamento | tuple:
        if identificador is not None:
            medicamento = self._db.search(
                target_db="medicamentos", target_field="identificador", search_value=identificador, lazy_mode=False
            )
            return medicamento

        return tuple(self._db.read(target_db="medicamentos").values())

    def buscar_medicamento(self) -> None:
        busca = input("Digite os termos de busca separados por vírgula: ")
        termos = [termo.strip() for termo in busca.split(",")]

        resultados = []
        for termo in termos:
            resultados_termo = self._db.search(
                target_db="medicamentos", target_field="descricao",
                search_value=termo, lazy_mode=True, return_first=False
            )
            resultados.extend(resultados_termo)

        if len(resultados) == 0:
            print("Nenhum medicamento foi encontrado para os termos de busca informados!")
            return None

        for resultado in resultados:
            print(resultado.__str__())

    def cadastrar_medicamento(self) -> None:
        nome = ""
        while len(nome) == 0:
            nome = input("Digite o nome do medicamento: ")
            if len(nome) == 0:
                print("Nome inválido!")

        principal_composto = ""
        while len(principal_composto) == 0:
            principal_composto = input("Digite o principal composto do medicamento: ")
            if len(principal_composto) == 0:
                print("Composto inválido")

        laboratorio = None
        labs = self._db.read("laboratorios").values()
        labs_nomes = [lab.nome for lab in labs]
        for lab in labs:
            print(lab)
            print("- - - - - - - - - - - - - - - - ")
        while laboratorio not in labs_nomes:
            laboratorio = input("Digite o nome do laboratório: ")
            if laboratorio not in labs_nomes:
                print("Nome inválido!")

        laboratorio = self._db.search(
            target_db="laboratorios", target_field="nome", search_value=laboratorio, lazy_mode=False
        )

        descricao = ""
        while len(descricao) == 0:
            descricao = input("Digite a descrição do medicamento: ")
            if len(descricao) == 0:
                print("Descrição inválida")

        valor = ""
        while len(valor) == 0:
            valor = input("Digite o valor do medicamento: ")
            if len(valor) == 0:
                print("Valor inválido!")

        valor = float(valor)

        tipo_medicamento = ""
        while len(tipo_medicamento) == 0:
            tipo_medicamento = input(
                'Qual o tipo de medicamento a ser cadastrado? F para Fitoterápico, Q para Quimioterápico.: '
            ).upper()
            if len(tipo_medicamento) == 0 or valor != "F" or valor != "Q":
                print("Valor inválido!")

        necessita_receita = input('O remédio necessita de receita? Digite S para Sim ou N para Não: ')
        receita_necessaria = True if necessita_receita == "S" else False

        identificador = self._db.gen_new_data_idx(target_db="medicamentos")
        novo_medicamento = Medicamento(identificador, nome, principal_composto, laboratorio, descricao, valor,
                                       receita_necessaria, tipo_medicamento)

        self._db.write(data=novo_medicamento)
        print(f"Medicamento cadastrado com sucesso! Código: {identificador}.")
