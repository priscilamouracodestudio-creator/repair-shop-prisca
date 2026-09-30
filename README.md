# 🏍️🛠️ Prisca Repair & Customization

Um sistema de linha de comando (CLI) robusto para gerenciamento de ordens de serviço e customização de motocicletas. O projeto aplica conceitos avançados de **Orientação a Objetos (POO)** e garante a persistência dos dados utilizando o banco de dados relacional **SQLite**.



## 🚀 Funcionalidades

- **Cadastro Dinâmico de Motocicletas:** Suporte a diferentes categorias de motos (Custom e Sports), coletando atributos específicos para cada tipo.
- **Gerenciamento de Ordens de Serviço:** Adição de manutenções e modificações em tempo real.
- **Atualização de Status e Orçamento:** Controle total sobre o andamento do serviço e valores estimados diretamente pelo menu.
- **Persistência com SQL:** Armazenamento seguro utilizando o comando `REPLACE INTO`, evitando duplicidade de registros e mantendo o histórico atualizado no arquivo `.db`.

---

## 🏗️ Arquitetura do Sistema (POO)

O projeto foi estruturado seguindo os pilares da Programação Orientada a Objetos:

- **Herança & Polimorfismo:** `CustomMoto` e `SportsMoto` herdam da classe base `Motorcycle`. A classe `OrderOfService` aceita qualquer subclasse de forma polimórfica.
- **Encapsulamento:** Atributos internos como `_service_status` e `_estimated_cost` são protegidos e modificados apenas através de métodos validados (`change_status` e `define_budget`).
- **Composição:** A classe `OrderOfService` possui um objeto do tipo `Motorcycle` associado a ela.

---

## 🗄️ Estrutura do Banco de Dados

Os dados são salvos na tabela `orders` dentro do arquivo `repairshop.db`:

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | INTEGER | Chave Primária (Autoincrement) |
| `brand` / `model` / `color` | TEXT | Dados estéticos da motocicleta |
| `year` / `engine_displacement` | INTEGER | Dados técnicos da motocicleta |
| `bike_type` | TEXT | Categoria (Custom / Sports) |
| `services` | TEXT | Lista de serviços executados (String formatada) |
| `budget` | REAL | Valor total estimado da ordem |
| `status` | TEXT | Status atual do serviço |

---

## 💻 Como Rodar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou navegue até a pasta do projeto:
   ```bash
   cd repairshop

---
📜 Licença
Este projeto foi desenvolvido para fins acadêmicos e de portfólio pessoal.

"See you space cowboy..." 🏍️💨