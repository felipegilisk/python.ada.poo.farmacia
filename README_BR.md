<img align="right" src="https://ada-site-frontend.s3.sa-east-1.amazonaws.com/home/header-logo.svg" style="width: 96px;" alt="Ada Tech Logo" />

## Sistema Integrado de Gestão de Farmácias (SIGFarm-ADA)

> Este projeto está relacionado ao segundo módulo da trilha de Engenharia de Dados, Programação Orientada à Objetos (POO), do programa da Ada Tech em parceria com o Santander, nomeado Santander Coders 2023. O propósito deste repositório é para centralizar todo o processo de desenvolvimento do Sistema Integrado de Gestão de Farmácias (com codenome `HLLNS-ADASC23-SIGFarm`), feito pelo time de desenvolvimento deste projeto.<br><br> To see the English version of this README, click <a href="https://github.com/felipegilisk/python.ada.poo.farmacia/blob/main/README.md">here</a>.

---

## 🚀 Como executar:
> Disclaimer: Este projeto foi desenvolvido utilizando o **Python 3.10** como versão base (mínima). Se você possui uma versão anterior, será necessário atualizar. Caso contrário, o código deste projeto não irá executar.

### 1. Clone este repositório

~~~shell
git clone git@github.com:felipegilisk/python.ada.poo.farmacia.git
~~~

### 2. Acesse a pasta do projeto
~~~shell
cd python.ada.poo.farmacia/
~~~

### 3. Execute o arquivo principal do projeto
~~~shell
python3 farmacia.py
~~~

---

## 🗂️ Estrutura das pastas

#### A estrutura utilizada para organizar este repositório/projeto toma como base a Metodologia MVC (Model, View, Controller).

- 📂 `controller/` - Pacote Python contendo todos os Controladores deste projeto. 
    - 🔖 `Cliente.py` - Módulo Python para o controlador dos usuários/clientes (classe `ClienteController`).
    - 🔖 `Medicamento.py` - Módulo Python para o controlador dos Medicamentos (classe `MedicamentoController`).
    - 🔖 `Venda.py` - Módulo Python para o controlador das Vendas (classe `VendaController`).
- 📂 `database/` - Pacote Python contendo todos os módulos relacionados ao gerenciamento de dados do projeto.
    - 📂 `data/` - Pasta contendo todos os arquivos de persistência `JSON` para a base com o `FileDB Engine`. 
    - 🔖 `Core.py` - Módulo Python para o `FileDB Engine` desenvolvido para este projeto (classe `FarmaciaFileDB`).
- 📂 `models/` - Pacote Python contendo todos os módulos de modelos para o projeto. 
    - 🔖 `Cliente.py` - Módulo Python para o modelo de Cliente (classe `Cliente`).
    - 🔖 `Laboratorio.py` - Módulo Python para o modelo de Laboratório (classe `Laboratorio`).
    - 🔖 `Medicamento.py` - Módulo Python para o modelo de Medicamento (classe `Medicamento`).
    - 🔖 `Venda.py` - Módulo Python para o modelo de Venda (classe `Venda`).
- 🔖 `farmacia.py` - Executável Python principal para o sistema.
---

<h3 style="text-align: justify;">
  ⚙️ Equipe de Desenvolvimento
</h3>

<table style="display: flex; align-itens: center; justify-content: center;">
  <tr>
    <td align="center"><a href="https://github.com/"><img style="width: 150px; height: 150;" src="https://www.kindpng.com/picc/m/106-1068191_transparent-avatar-clipart-hd-png-download.png" width="100px;" alt=""/><br /><sub><b>Henrique Napoleão</b></sub></a><br /><sub><b>---</sub></a></td>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Rodrigues</b></sub></a><br /><sub><b>Data Engineer</sub></a></td>
    <td align="center"><a href="https://github.com/felipegilisk"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/95372771?v=4" alt=""/><br /><sub><b>Luis Gilisk</b></sub></a><br /><sub><b>Python Developer</sub></a></td>
    <td align="center"><a href="https://github.com/csonicholas"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/108910737?v=4" alt=""/><br /><sub><b>Nicholas Oliveira</b></sub></a><br /><sub><b>Python Developer</sub></a></td>
    <td align="center"><a href="https://github.com/"><img style="width: 150px; height: 150;" src="https://www.kindpng.com/picc/m/106-1068191_transparent-avatar-clipart-hd-png-download.png" alt=""/><br /><sub><b>Stéfanni Santos</b></sub></a><br /><sub><b>Python Developer</sub></a></td>
  </tr>
<table>

---

###### Última atualização: Agosto 20, 2023. Autor: Lucas Rodrigues (@NepZR | lucas.darlindo@gmail.com).