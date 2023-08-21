<img align="right" src="https://ada-site-frontend.s3.sa-east-1.amazonaws.com/home/header-logo.svg" style="width: 96px;" alt="Ada Tech Logo" />

## Sistema Integrado de Gestão de Farmácias (SIGFarm-ADA)

> This project is related to the second module of the Data Engineering Track, Object-oriented programming (OOP), of Ada Tech's Program in collaboration with Santander, named Santander Coders 2023. The purpose of this repository is to centralize all development of the Integrated Pharmacy Management System (codenamed `HLLNS-ADASC23-SIGFarm`), made by the development team in this project.<br><br> Para visualizar a versão em Português do Brasil deste README, clique <a href="https://github.com/felipegilisk/python.ada.poo.farmacia/blob/main/README_BR.md">aqui</a>.

---

## 🚀 How to Run:
> Disclaimer: this project was developed using **Python 3.10** as a base version. If you have a Previous Python Version, upgrade is needed. Otherwise, **the code will not run**.

### 1. Clone the repository

~~~shell
git clone git@github.com:felipegilisk/python.ada.poo.farmacia.git
~~~

### 2. Access the Project Folder
~~~shell
cd python.ada.poo.farmacia/
~~~

### 3. Run the Main Python Executable Script
~~~shell
python3 farmacia.py
~~~

---

## 🗂️ Folder Structure

#### The structure used for organizing this repository follows the MVC Methodology.

- 📂 `controller/` - Python Package containing all Controller Modules. 
    - 🔖 `Cliente.py` - Python Module for the User Controller (class `ClienteController`).
    - 🔖 `Medicamento.py` - Python Module for the Drug Controller (class `MedicamentoController`).
    - 🔖 `Venda.py` - Python Module for the Sale Controller (class `VendaController`).
- 📂 `database/` - Python Package containing all modules related to the data management of this system.
    - 📂 `data/` - Folder containing the persistent `JSON` database files for the `FileDB Engine`. 
    - 🔖 `Core.py` - Python Module for the `FileDB Engine` developed for this project (class `FarmaciaFileDB`).
- 📂 `models/` - Python Package containing all Model Modules with its classes. 
    - 🔖 `Cliente.py` - Python Module for the User Model (class `Cliente`).
    - 🔖 `Laboratorio.py` - Python Module for the Laboratory Model (class `Laboratorio`).
    - 🔖 `Medicamento.py` - Python Module for the Drug Model (class `Medicamento`).
    - 🔖 `Venda.py` - Python Module for the Sale Model (class `Venda`).
- 🔖 `farmacia.py` - Main Python Executable for the system.
---

<h3 style="text-align: justify;">
  ⚙️ Development Team
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

###### Last Updated: August 20th, 2023. Author: Lucas Rodrigues (@NepZR | lucas.darlindo@gmail.com).