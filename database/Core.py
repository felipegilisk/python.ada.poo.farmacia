import json
import os
from copy import deepcopy
from datetime import datetime
from typing import Tuple, List

from model.Cliente import Cliente
from model.Laboratorio import Laboratorio
from model.Medicamento import Medicamento
from model.Venda import Venda


class FarmaciaFileDB:
    def __init__(self) -> None:
        self._mode = "json"
        self._data_path = "database/data/"
        self._mapping = self._retrieve_data_mapping()
        self._data = self._load_persistent_data()

        self._remap_data_phase_1()
        self._remap_data_phase_2()

    def _retrieve_data_mapping(self) -> dict:
        data_mapping = {
            "clientes": {
                "file": f"{self._data_path}clientes.{self._mode}",
                "map": ("cpf", "nome", "data_nascimento"),
                "class": Cliente
            },
            "laboratorios": {
                "file": f"{self._data_path}laboratorios.{self._mode}",
                "map": ("nome", "telefone", "endereco", "cidade", "estado"),
                "class": Laboratorio
            },
            "medicamentos": {
                "file": f"{self._data_path}medicamentos.{self._mode}",
                "map": (
                    "identificador", "nome", "principal_composto", "laboratorio",
                    "descricao", "valor_unitario", "receita_necessaria", "tipo_medicamento"
                ),
                "class": Medicamento
            },
            "vendas": {
                "file": f"{self._data_path}vendas.{self._mode}",
                "map": ("momento_venda", "cliente", "produtos", "valor_venda"),
                "class": Venda
            },
        }
        return data_mapping

    def _load_persistent_data(self) -> dict:
        database = {}
        for target_db in self._mapping.keys():
            print(f"FileDB Engine | Carregar >> Carregando arquivo JSON de persistência para a base \"{target_db}\".")
            with open(self._mapping[target_db]["file"], "r") as file_db:
                database[target_db] = json.loads(file_db.read())

        print(f"FileDB Engine | Carregar >> Carregamento da base persistente para a memória bem-sucedido.")
        return database

    def gen_new_data_idx(self, target_db: str) -> str:
        if target_db not in self._mapping.keys():
            raise ValueError(f"FarmáciaDB | Busca >> A base de dados \"{target_db}\" não existe.")

        if len(self._data[target_db].keys()) == 0:
            new_data_idx = 0
        else:
            new_data_idx = f"{max(map(int, self._data[target_db].keys())) + 1}"
        return new_data_idx

    def _map_new_data(self, staged_data: Cliente | Laboratorio | Medicamento | Venda) -> Tuple[str, dict]:
        """
        Realiza o mapeamento dos novos dados a serem inseridos na base ativa em memória (update/index) e para o arquivo
        de persistência (JSON).

        Parameters:
            staged_data (Cliente | Laboratorio | Medicamento | Venda): Objeto a ser escrito na base de dados.
        """
        if isinstance(staged_data, Cliente):
            target_db = "clientes"
        elif isinstance(staged_data, Laboratorio):
            target_db = "laboratorios"
        elif isinstance(staged_data, Medicamento):
            target_db = "medicamentos"
        elif isinstance(staged_data, Venda):
            target_db = "vendas"
        else:
            raise TypeError("FarmáciaDB | Escrita >> Formato desconhecido ou não mapeado na base de dados.")

        new_data_idx = self.gen_new_data_idx(target_db=target_db)
        final_staged_data = {f"{new_data_idx}": staged_data.__dict__()}

        self._data[target_db].update({f"{new_data_idx}": staged_data})
        print(f"FarmáciaDB | Escrita >> Base de dados \"{target_db}\" EM MEMÓRIA atualizada com sucesso.")

        return target_db, final_staged_data

    def _remap_data_phase_2(self) -> None:
        remapped_sell_db = {}
        sell_database = deepcopy(self._data["vendas"])
        if len(sell_database.keys()) > 0:
            for idx in sell_database.keys():
                produtos = [
                    produto for produto in [
                        self.search(
                            target_db="medicamentos", target_field="identificador", search_value=prod_id, lazy_mode=False
                        ) for prod_id in sell_database[idx]["produto_ids"]
                    ]
                ]
                cliente = self.search(
                    target_db="clientes", target_field="cpf", search_value=sell_database[idx]["cliente"], lazy_mode=False
                )
                momento_venda = datetime.strptime(sell_database[idx]["momento_venda"], "%Y-%m-%d %H:%M:%S")
                remapped_sell_db[idx] = Venda(momento_venda, produtos, cliente)

            self._data["vendas"] = remapped_sell_db

        print(f"FileDB Engine | Inicialização (Fase 2) >> Remapeamento final da base de dados bem-sucedida.")
        os.system("clear" if os.name != "nt" else "cls")

    def _remap_data_phase_1(self) -> None:
        print(f"FileDB Engine | Inicialização >> Executando remapeamento de objetos para a base de dados em memória.")
        for target_db in self._mapping.keys():
            if target_db == "vendas":
                continue
            obj_class = self._mapping[target_db]["class"]
            mapped_db = {}
            for idx in self._data[target_db].keys():
                unmapped_data = self._data[target_db][idx]
                print(unmapped_data)
                mapped_obj = obj_class(**unmapped_data)
                mapped_db[idx] = mapped_obj

            self._data[target_db] = mapped_db

        print(f"FileDB Engine | Inicialização (Fase 1) >> Remapeamento da base de dados bem-sucedida.")

    @staticmethod
    def _remap_for_write(data: dict) -> dict:
        """
        Realiza o remapeamento dos dados da base informada para o formato JSON-Compatible, permitindo a escrita no
        arquivo de persistência.

        Parameters:
            data (dict): Base de dados em memória com o mapeamento Key: Object original.

        Returns:
            dict: Base de dados em dict remapeada e compatível para escrita em formato JSON.
        """
        remaped_data = {
            idx: obj_data.__dict__()
            for idx, obj_data in zip(data.keys(), data.values())
        }
        return remaped_data

    def write(self, data: Cliente | Laboratorio | Medicamento | Venda) -> None:
        """
        Realiza a escrita dos dados na base de dados ativa em Memória e atualiza o arquivo de persistência JSON da base.

        Parameters:
            data (Cliente | Laboratorio | Medicamento | Venda): Objeto para ser escrito na base de dados.
        """
        target_data, _ = self._map_new_data(staged_data=data)
        with open(f"{self._mapping.get(target_data)['file']}", "w", newline='', encoding="UTF-8") as target_file_db:
            remapped_data = self._remap_for_write(data=self._data[target_data])
            json.dump(remapped_data, target_file_db, ensure_ascii=False, indent=4)

        print(f"FarmáciaDB | Escrita >> Base de dados \"{target_data}\" PERSISTENTE atualizada com sucesso.")

    def read(self, target_db: str) -> dict:
        """
        Realiza a leitura dos dados na base de dados ativa em Memória.

        Parameters:
            target_db (str): String case-insensitive para identificar a base a ser recuperada.

        Returns:
            dict: Base de dados alvo contendo os dados carregados e ativos em memória.
        """
        valid_target = False
        for valid_db in self._mapping.keys():
            if valid_db == target_db.lower().strip():
                valid_target = True
                break

        if not valid_target:
            raise ValueError(f"FarmáciaDB | Leitura >> A base de dados \"{target_db}\" não existe.")

        return self._data[target_db]

    def search(
            self, target_db: str, target_field: str, search_value: str,
            lazy_mode: bool = True, return_first: bool = True
    ) -> Cliente | Laboratorio | Medicamento | Venda | Tuple[Cliente | Laboratorio | Medicamento | Venda] | None:
        if target_db not in self._mapping.keys():
            raise ValueError(f"FarmáciaDB | Busca >> A base de dados \"{target_db}\" não existe.")
        if target_field not in self._mapping[target_db]["map"]:
            raise ValueError(
                f"FarmáciaDB | Busca >> A chave \"{target_field}\" não é valida para a base \"{target_db}\"."
            )

        target_db_data = self.read(target_db=target_db)
        match_data: List[Cliente | Laboratorio | Medicamento | Venda] = []
        for db_idx in target_db_data.keys():
            db_object = target_db_data[db_idx].__getattribute__(target_field)
            if lazy_mode:
                match = search_value in db_object
            else:
                match = search_value == db_object

            if match and return_first:
                return target_db_data[db_idx]
            if match and not return_first:
                match_data.append(target_db_data[db_idx])

        if not return_first:
            return tuple(match_data)

        return None
