# Sistema de Login

## Descrição

Este projeto é um sistema básico de login de usuários, utilizando Python, SQLite, Dash e bcrypt para criptografia de senhas.
O sistema permite criar novos usuários, fazer login com verificação de senha segura e armazenar as informações no banco de dados SQLite.

O código foi modularizado para seguir as boas práticas, com a separação das telas em arquivos específicos,
além das lógicas tanto do banco de dados, como da criptografia de senhas, sendo alocadas em arquivos diferentes.

## Funcionalidades

- Criação de usuários com nome de usuário, email e senha hasheada.
- Login com verificação de senha utilizando bcrypt.
- Armazenamento dos dados no banco de dados SQLite.
- Modularização do código para facilitar a manutenção e segurança.

## Requisitos
- Python 3.7 ou superior
- Bibliotecas Python:
  - `bcrypt`
  - `dash`
  - `dash_bootstrap_components`
  - `sqlite3` (incluso por padrão no Python)
